Postgres + Redis: docker compose up -d  
Fast API start: uvicorn main:app -reload  

Getting Started  
---------------  
1. Start Postgres and Redis using Docker:  
   `docker compose up -d`  

2. Run FastAPI with reload for development:  
   `uvicorn main:app -reload`  

Running the Application  
-----------------------  
To test distributed systems with Redis:  
- Start multiple uvicorn workers:  
  `uvicorn main:app --workers 4`  

Testing WebSockets  
------------------  
After starting the server:  
1. Open `app/websocket/test_websockets.html` in a browser  
2. Test real-time communication across workers  

Prerequisites  
-------------  
- Docker (for Postgres/Redis)  
- uvicorn (FastAPI server)  
- Python 3.10+  

Note: Ensure Docker is running before starting services. Multiple workers simulate distributed system behavior for WebSocket testing.