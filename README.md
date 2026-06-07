Postgres + Redis: docker compose up -d  
Fast API start: uvicorn main:app --reload  

## Getting Started  
1. Start Postgres and Redis with Docker:  
   ```bash  
   docker compose up -d  
   ```  

2. Run FastAPI application:  
   ```bash  
   uvicorn main:app --reload  
   ```  

## Testing Distributed Systems  
To test socket communication in distributed systems using Redis:  
1. Start multiple Uvicorn workers:  
   ```bash  
   uvicorn main:app --workers 4  
   ```  

2. Access the test interface:  
   Open `app/websocket/test_websockets.html` in your browser.  

## Notes  
- Ensure Docker is installed before running the Postgres/Redis setup.  
- The `--workers 4` flag enables parallel processing for distributed testing.