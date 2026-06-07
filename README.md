Distributed System Communication Demo

## Getting Started

To start the Postgres and Redis services using Docker:
```bash
docker compose up -d
```

## Running the Application

To start the FastAPI server:
```bash
uvicorn main:app -reload
```

To run the server with multiple workers for distributed testing:
```bash
uvicorn main:app --workers 4
```

## Testing WebSockets

After starting the server, navigate to the test interface:
```
app/websocket/test_websockets.html
```