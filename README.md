Postgres + Redis: docker compose up -d  
Fast API start: uvicorn main:app --reload  

## Running the Application  

### 1. Start Services  
```bash  
docker compose up -d  
```  

### 2. Run FastAPI with Multiple Workers (for distributed testing)  
```bash  
uvicorn main:app --workers 4  
```  

### 3. Test WebSockets  
Open the following file in a browser:  
`app/websocket/test_websockets.html`  

This setup enables testing of WebSocket communication across distributed systems using Redis.