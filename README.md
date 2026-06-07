# Project Overview

This project demonstrates a FastAPI application using Postgres and Redis for database and caching needs. It includes WebSocket support for distributed system communication testing.

## Getting Started

### Setting Up Dependencies
1. Ensure Docker is installed
2. Start Postgres and Redis with Docker:
```bash
docker compose up -d
```

### Running the Application

#### Basic Start
```bash
uvicorn main:app --reload
```

#### Testing with Multiple Workers
To test distributed WebSocket communication:
```bash
uvicorn main:app --workers 4
```

#### Testing WebSockets
After starting the application:
1. Open `app/websocket/test_websockets.html` in your browser
2. Test WebSocket connections across multiple workers

## Notes
- The application uses Redis for inter-worker communication
- Postgres is used for persistent data storage
- WebSocket testing demonstrates communication in distributed systems