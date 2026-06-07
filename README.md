Postgres + Redis: Start services with Docker Compose  
FastAPI: Launch the application with Uvicorn  

## Setup Instructions  
To start the Postgres and Redis services, use Docker Compose:  
```bash  
docker compose up -d  
```  

## Running the Application  
Start the FastAPI server in development mode:  
```bash  
uvicorn main:app --reload  
```  

For testing distributed systems with Redis, run multiple Uvicorn workers:  
```bash  
uvicorn main:app --workers 4  
```  

## Testing WebSockets  
After starting the server, navigate to the following file in your browser:  
`app/websocket/test_websockets.html`  

## Notes  
- Ensure Docker is installed and running before executing the setup command.  
- The `--workers 4` flag enables parallel processing for WebSocket testing.  
- The `test_websockets.html` file is part of the application's frontend for testing purposes.