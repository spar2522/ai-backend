Distributed Systems Communication with FastAPI, Postgres, and Redis

## Getting Started

### Prerequisites
- Docker installed on your machine

### Setup
1. Start Postgres and Redis containers using Docker:
```bash
docker compose up -d
```

## Running the Application

### Development Mode
To start the FastAPI application with auto-reload:
```bash
uvicorn main:app --reload
```

### Production Mode
For testing distributed systems with multiple workers:
```bash
uvicorn main:app --workers 4
```

## Testing
After starting the application:
1. Open the test interface in your browser:
```bash
app/websocket/test_websockets.html
```
This page contains WebSocket test clients for verifying communication across distributed system components.