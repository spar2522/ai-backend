# README

## Overview
Project setup and usage instructions for a FastAPI application with Postgres and Redis.

## Getting Started

### Prerequisites
- Docker
- Docker Compose
- Python 3.8+

### Setup
1. Start Postgres and Redis containers:
```bash
docker compose up -d
```

### Starting the FastAPI Server
To start the application:
```bash
uvicorn main:app --reload
```

For testing distributed systems with multiple workers:
```bash
uvicorn main:app --workers 4
```

### Testing WebSockets
1. Open browser and navigate to:
```
app/websocket/test_websockets.html
```
2. Test WebSocket communication across multiple workers

## Notes
- Ensure Docker is running before executing container commands
- The `--reload` flag enables hot reload during development
- Multiple workers simulate distributed system environments
- Redis is used for inter-worker communication testing