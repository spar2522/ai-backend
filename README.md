# Setup Instructions

## Prerequisites
- Docker installed
- Python 3.8+

## Start Services
To start Postgres and Redis containers:
```bash
docker compose up -d
```

## Start FastAPI Application
To start the FastAPI application:
```bash
uvicorn main:app --reload
```

## Run with Multiple Workers
To run the application with 4 workers for testing distributed systems:
```bash
uvicorn main:app --workers 4
```

## Testing WebSockets
After starting the application:
1. Navigate to `app/websocket/test_websockets.html`
2. Test WebSocket connections across distributed workers