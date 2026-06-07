Postgres + Redis: docker-compose up -d  
FastAPI Start: uvicorn main:app --reload  

## Getting Started  
1. **Start dependencies**  
   Run the following command to start Postgres and Redis using Docker:  
   ```bash  
   docker-compose up -d  
   ```  

2. **Run FastAPI application**  
   Start the FastAPI server with automatic reloading:  
   ```bash  
   uvicorn main:app --reload  
   ```  

## Testing WebSocket Communication  
To test distributed system communication via Redis:  
1. **Run multiple workers**  
   Execute the following command to start the FastAPI server with 4 parallel workers:  
   ```bash  
   uvicorn main:app --workers 4  
   ```  

2. **Access test interface**  
   Open the WebSocket test interface in your browser:  
   ```  
   Navigate to `app/websocket/test_websockets.html`  
   ```  

## Notes  
- Ensure Docker is installed and running before executing `docker-compose up -d`.  
- The `main:app` reference assumes a FastAPI application is defined in `main.py`.  
- Use `--workers N` to adjust the number of parallel workers for testing.