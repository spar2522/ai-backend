# Project Overview

This project demonstrates a FastAPI application using Postgres and Redis for distributed system communication testing.

## Prerequisites
- Docker installed
- Python 3.8+

## Setup and Configuration

### Start Dependencies
```bash
docker compose up -d
```

### Run FastAPI Application
For development:
```bash
uvicorn main:app --reload
```

For distributed testing with 4 workers:
```bash
uvicorn main:app --workers 4
```

## Testing
To test WebSocket communication:
1. Open `app/websocket/test_websockets.html` in your browser
2. Observe distributed system communication across Redis

## Notes
- The WebSocket test suite validates cross-worker communication
- Redis is used for message passing between workers
- Postgres is available for data persistence needs