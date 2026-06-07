Postgres + Redis: Start services using Docker  
```bash
docker compose up -d
```

FastAPI Startup: Launch the application  
```bash
uvicorn main:app --reload
```

For testing distributed systems with Redis:  
Start multiple workers  
```bash
uvicorn main:app --workers 4
```

Test WebSockets:  
Navigate to the following file in your browser:  
`app/websocket/test_websockets.html`