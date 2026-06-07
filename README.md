# Project Setup and Usage Instructions

## Getting Started

To start the Postgres and Redis services using Docker, run the following command:

```bash
docker compose up -d
```

This will start the containers in detached mode.

## Running the FastAPI Application

To start the FastAPI application with auto-reload for development:

```bash
uvicorn main:app --reload
```

For testing distributed systems with Redis, run the application with multiple workers:

```bash
uvicorn main:app --workers 4
```

## Testing WebSocket Communication

To test WebSocket connections and communication in distributed systems:

1. Open the following file in your browser:
   ```
   app/websocket/test_websockets.html
   ```

This file provides an interface to test WebSocket communication across multiple workers.