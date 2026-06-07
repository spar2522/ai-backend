Postgres + Redis: docker compose up -d  
Fast API start: uvicorn main:app -reload  

To run FastAPI with multiple workers for testing distributed systems:  
uvicorn main:app --workers 4  

Open the WebSocket test interface:  
app/websocket/test_websockets.html