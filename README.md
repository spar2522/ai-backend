Postgres + Redis: docker compose up -d
Fast API start : uvicorn main:app --reload 

To have parallel uvicorn workers to test socket connections and communication in distributed systems using Redis
uvicorn main:app --workers 4 
Open the test_websockets.html file in your browser located at app/websocket/test_websockets.html