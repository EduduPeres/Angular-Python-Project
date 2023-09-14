from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send(self, item: dict, websocket: WebSocket):
        await websocket.send_json(item)

    async def broadcast(self, item: dict):
        for connection in self.active_connections:
            await connection.send_json(item)

manager = ConnectionManager()