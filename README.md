# README

## Getting Started

To set up the project, follow these steps:

1. Start Postgres and Redis using Docker:
   ```
   docker compose up -d
   ```

2. Run the FastAPI application:
   ```
   uvicorn main:app --reload
   ```

## Running with Multiple Workers

To test distributed systems with Redis, start the application with multiple workers:
```
uvicorn main:app --workers 4
```

## Testing WebSockets

To test WebSocket communication:
1. Open the file located at `app/websocket/test_websockets.html`
2. Use this interface to test connections across distributed workers