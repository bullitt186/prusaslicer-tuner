"""Thin client for a self-hosted Prusa Connect (prusa3d/prusa-connect) and PrusaLink as fallback.

Env: CONNECT_URL, CONNECT_TOKEN (or CONNECT_TOKEN_FILE), CONNECT_STORAGE (default "local").
PrusaLink fallback per printer: PRUSALINK_<NAME>=http://user:password@host (NAME upper-case).
Connect Local is a 0.x beta; endpoints follow its OpenAPI of 0.1.0-beta.1.
"""
import json, os, time, urllib.error, urllib.parse, urllib.request

SLICING = "com.github.aux.prusa3d.server-slicing"


class ConnectError(RuntimeError):
    pass


def _base():
    url = os.environ.get("CONNECT_URL", "").rstrip("/")
    if not url:
        raise ConnectError("CONNECT_URL is not set")
    return url


def _token():
    tok = os.environ.get("CONNECT_TOKEN")
    if not tok and os.environ.get("CONNECT_TOKEN_FILE"):
        with open(os.environ["CONNECT_TOKEN_FILE"], encoding="utf-8") as f:
            tok = f.read().strip()
    if not tok:
        raise ConnectError("CONNECT_TOKEN or CONNECT_TOKEN_FILE is not set")
    return tok


def storage():
    return os.environ.get("CONNECT_STORAGE", "local")


def _call(method, path, body=None, ctype="application/json", query=None, timeout=60):
    url = _base() + path + ("?" + urllib.parse.urlencode(query) if query else "")
    data = body if isinstance(body, (bytes, type(None))) else json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Authorization": f"Bearer {_token()}", "Content-Type": ctype,
                                          "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:  # RFC 9457 problem: code + detail + trace_id
        try:
            p = json.loads(e.read())
            raise ConnectError(f"{e.code} {p.get('code', '')}: {p.get('detail') or p.get('title')} "
                               f"(trace {p.get('trace_id', '-')})") from None
        except ValueError:
            raise ConnectError(f"{e.code} {e.reason} on {method} {path}") from None
    return json.loads(raw) if raw else {}


def upload(path, data):
    """Put bytes into the Connect storage at `path`; returns the storage's answer (with sha256)."""
    return _call("PUT", f"/api/v1/storages/{storage()}/content", data, "application/octet-stream",
                 {"path": path}, timeout=300)


def slice_job(path, output=None, slicer=None, overwrite=True):
    body = {"source": {"storage": storage(), "path": path}, "format": "bgcode", "overwrite": overwrite}
    if output:
        body["output"] = {"storage": storage(), "path": output}
    if slicer:
        body["slicer"] = slicer
    return _call("POST", f"/api/v1/modules/{SLICING}/jobs", body)


def job(job_id):
    return _call("GET", f"/api/v1/modules/{SLICING}/jobs/{urllib.parse.quote(str(job_id))}")


def wait_job(job_id, timeout=900, every=3):
    end = time.monotonic() + timeout
    while True:
        j = job(job_id)
        if j.get("state") in ("done", "failed", "canceled"):
            return j
        if time.monotonic() > end:
            raise ConnectError(f"slicing job {job_id} still {j.get('state')} after {timeout}s")
        time.sleep(every)


def slicers():
    return _call("GET", f"/api/v1/modules/{SLICING}/slicers")


def devices():
    return _call("GET", "/api/v1/devices").get("items", [])


def device(ref):
    """Device by id, name, serial or unit_uid (case-insensitive)."""
    for d in devices():
        if ref.lower() in {str(d.get(k, "")).lower() for k in ("id", "name", "serial", "unit_uid")}:
            return d
    raise ConnectError(f"no device '{ref}' on this Connect")


def start_print(device_id, source, name, replace=False):
    """Relay a stored file to the printer's USB storage and start it, in one call."""
    body = {"storage": storage(), "source": source, "path": f"usb/{name}", "replace": replace}
    return _call("POST", f"/api/v1/devices/{device_id}/print", body, timeout=900)


def download(path):
    req = urllib.request.Request(_base() + f"/api/v1/storages/{storage()}/content?" + urllib.parse.urlencode({"path": path}),
                                 headers={"Authorization": f"Bearer {_token()}"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


def prusalink_print(printer, name, data):
    """Fallback without Connect: PrusaLink upload with Print-After-Upload (HTTP Digest)."""
    url = os.environ.get(f"PRUSALINK_{printer.upper().replace(' ', '_').replace('-', '_')}")
    if not url:
        raise ConnectError(f"no PRUSALINK_{printer.upper()} configured for the fallback")
    u = urllib.parse.urlsplit(url)
    host = f"{u.scheme}://{u.hostname}" + (f":{u.port}" if u.port else "")
    pw = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pw.add_password(None, host, urllib.parse.unquote(u.username or ""), urllib.parse.unquote(u.password or ""))
    opener = urllib.request.build_opener(urllib.request.HTTPDigestAuthHandler(pw))
    req = urllib.request.Request(f"{host}/api/v1/files/usb/{urllib.parse.quote(name)}", data=data, method="PUT",
                                 headers={"Content-Type": "application/octet-stream", "Print-After-Upload": "?1",
                                          "Overwrite": "?1"})
    with opener.open(req, timeout=600) as r:
        return {"status": r.status}
