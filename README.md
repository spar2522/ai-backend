# Project Setup and Usage Guide

## Overview
This project demonstrates WebSocket communication in distributed systems using Redis as a message broker. It includes a FastAPI backend with Postgres and Redis services managed via Docker.

## Getting Started

### Prerequisites
- Docker installed
- Python 3.8+

### Setup Services
Start Postgres and Redis containers using Docker:
```bash
docker compose up -d
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

### Basic Startup
To start the FastAPI server:
```bash
uvicorn main:app --reload
```

### Testing Distributed Systems
For testing WebSocket communication across multiple workers:
```bash
uvicorn main:app --workers 4
```

## Testing WebSockets
1. Open `app/websocket/test_websockets.html` in your browser
2. Observe WebSocket behavior across multiple worker processes
3. Verify message synchronization through Redis

## Notes
- The `--workers 4` flag demonstrates distributed system testing
- Redis handles message synchronization between workers
- Postgres is used for persistent data storage