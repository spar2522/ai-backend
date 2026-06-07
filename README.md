# Project Setup and Usage

## Prerequisites
- Docker installed and running.

## Starting Services
To start Postgres and Redis using Docker:
```bash
docker compose up -d
```

## Running the FastAPI Application
To start the FastAPI application with reload:
```bash
uvicorn main:app --reload
```

To run the application with multiple workers for testing distributed systems:
```bash
uvicorn main:app --workers 4
```

## Testing WebSockets
After starting the application, navigate to the following file to test websockets:
```
app/websocket/test_websockets.html
```