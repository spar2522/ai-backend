Postgres + Redis: docker compose up -d  
Fast API start: uvicorn main:app --reload  

Setup:  
- Start Postgres and Redis with Docker Compose  
- Run FastAPI with reload for development  

Testing with Multiple Workers:  
To simulate distributed systems and test Redis-based communication:  
uvicorn main:app --workers 4  

Testing WebSockets:  
Open the file: app/websocket/test_websockets.html in your browser