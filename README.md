Distributed System Testing with FastAPI, Postgres, and Redis

## Getting Started

### Prerequisites
- Docker installed on your system
- Python 3.8+

### Setup
1. Start Postgres and Redis containers:
```bash
docker compose up -d
```

## Running the Application

### Basic Start
To run the FastAPI application with reload:
```bash
uvicorn main:app --reload
```

### Distributed Testing
For testing WebSocket communication in distributed systems:
```bash
uvicorn main:app --workers 4
```

## Testing WebSocket Communication
1. Open your browser and navigate to:
```
app/websocket/test_websockets.html
```
This file contains test cases for WebSocket communication across multiple workers.