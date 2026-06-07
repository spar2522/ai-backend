# FastAPI with Postgres and Redis for Distributed System Testing

## Getting Started

To set up the environment:

1. **Start Postgres and Redis with Docker:**
   ```bash
   docker compose up -d
   ```
   *Ensure you run this command from the project root directory. Docker must be installed and running.*

2. **Start the FastAPI application:**
   ```bash
   uvicorn main:app --reload
   ```
   *This command starts the development server with hot reload enabled.*

## Testing WebSockets

To test WebSocket communication in distributed systems using Redis:

1. **Run multiple Uvicorn workers:**
   ```bash
   uvicorn main:app --workers 4
   ```
   *This configuration helps simulate distributed environments and test Redis-based communication across multiple workers.*

2. **Access the test interface:**
   Navigate to the following file in your browser:
   ```
   app/websocket/test_websockets.html
   ```
   *This page provides an interface to interact with and test WebSocket connections.*