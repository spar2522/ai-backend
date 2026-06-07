Postgres + Redis: docker compose up -d

## Getting Started

### Start Services
```bash
docker compose up -d
```

### Start FastAPI Application
```bash
uvicorn main:app --reload
```

## Testing

### Run with Multiple Workers
To test distributed systems with Redis:
```bash
uvicorn main:app --workers 4
```

### Access Test Interface
Open in browser:
```
http://localhost:8000/app/websocket/test_websockets.html
```

## Notes
- Ensure Docker is installed for containerized services
- The `docker-compose.yml` file includes Postgres and Redis configurations
- For production, consider using gunicorn with appropriate worker settings
- The `main.py` file contains the FastAPI application entry point