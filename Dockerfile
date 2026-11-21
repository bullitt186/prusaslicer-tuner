# MCP server over streamable-http, for slicing and printing through a self-hosted Prusa Connect.
# Mount the PrusaSlicer data dir read-only at /profiles; put auth in front (gateway or proxy).
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
WORKDIR /app
COPY . .
# Bake the PEP 723 dependencies so the container starts without network.
RUN uv export --script server.py > /tmp/req.txt && uv pip install --system -r /tmp/req.txt && rm /tmp/req.txt
ENV PRUSASLICER_DIR=/profiles MCP_TRANSPORT=streamable-http MCP_HOST=0.0.0.0 MCP_PORT=8000 \
    MODEL_CACHE=/tmp PROFILES_BACKUP_DIR=/tmp/backups
USER 10001
EXPOSE 8000
CMD ["python", "server.py"]
