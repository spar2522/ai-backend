Postgres + Redis: Start services with `docker compose up -d`  
FastAPI: Start the application with `uvicorn main:app --reload`  

To test distributed systems with Redis and multiple workers:  
Run `uvicorn main:app --workers 4`  
Access the WebSocket test interface at `app/websocket/test_websockets.html`  

---

### Setup  
1. Ensure Docker is installed and running  
2. Start Postgres and Redis:  
   ```bash  
   docker compose up -d  
   ```  

---

### Usage  
- **Development Mode**:  
  ```bash  
  uvicorn main:app --reload  
  ```  
- **Production/Testing with Multiple Workers**:  
  ```bash  
  uvicorn main:app --workers 4  
  ```  

---

### Testing  
- Open `app/websocket/test_websockets.html` in a browser  
- This interface demonstrates WebSocket communication across Redis-backed distributed systems  
- Multiple workers simulate real-world distributed behavior  

---

### Notes  
- Ensure all services (Postgres, Redis) are running before starting the FastAPI app  
- WebSocket testing requires browser support for WebSocket protocols  
- Worker count can be adjusted based on testing requirements