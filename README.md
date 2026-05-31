Postgres + Redis: docker compose up -d
Fast API start : uvicorn main:app -reload 

To have parallel uvicorn workers to test socket connections and commnication in distributed systems using Redis
uvicorn main:app --workers 4 
go to app->websocket->test_websockets.html
