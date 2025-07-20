#!/bin/bash
set -e

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

docker build -t fastapi-rbac-app .
docker rm -f fastapi-rbac-container 2>/dev/null || true
docker run -d --name fastapi-rbac-container -p 8000:8000 fastapi-rbac-app

echo "Setup complete. The FastAPI service is running in a Docker container on port 8000."
