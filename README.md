# README

## Setup

Start Postgres and Redis using Docker:

```bash
docker compose up -d
```

## Usage

To start the FastAPI application:

```bash
uvicorn main:app --reload
```

For testing distributed systems with Redis, run the application with multiple workers:

```bash
uvicorn main:app --workers 4
```

## Testing WebSockets

Navigate to the following file in your browser to test WebSocket communication:

```
app/websocket/test_websockets.html
```