# README.md

## Getting Started

To start the Postgres and Redis services using Docker, run:
```bash
docker compose up -d
```

## Starting the FastAPI Application

To start the FastAPI application with reload support:
```bash
uvicorn main:app --reload
```

## Testing WebSockets in Distributed Systems

To run the FastAPI application with multiple workers for testing WebSocket communication across distributed systems:
```bash
uvicorn main:app --workers 4
```

After starting the application, navigate to the following file in your browser to test WebSockets:
```
app/websocket/test_websockets.html
```