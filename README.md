Postgres + Redis: docker compose up -d  
Fast API start: uvicorn main:app --reload  

## Usage  

To run the FastAPI application with multiple workers for testing distributed system communication via Redis:  
```bash  
uvicorn main:app --workers 4  
```  

## Testing WebSockets  
Navigate to the following file in your browser to test WebSocket connections:  
`app/websocket/test_websockets.html`  

This setup demonstrates distributed system communication using Redis and multiple FastAPI workers.