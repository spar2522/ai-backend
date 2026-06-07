# FastAPI WebSocket Communication with Redis and Postgres

## Getting Started

### Prerequisites
- Docker installed
- Python 3.8+

### Setup
1. Start Postgres and Redis with Docker:
```bash
docker compose up -d
```

## Running the Application

### Basic Start
To run the FastAPI application:
```bash
uvicorn main:app --reload
```

### Testing Distributed Systems
For testing WebSocket communication in distributed systems:
```bash
uvicorn main:app --workers 4
```

## Testing WebSocket Communication
1. Open browser and navigate to:
```
app/websocket/test_websockets.html
```
This page demonstrates WebSocket communication across multiple workers using Redis.