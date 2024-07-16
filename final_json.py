from fastapi import FastAPI, WebSocketDisconnect
from fastapi.websockets import WebSocket


app = FastAPI()


@app.websocket("/")
async def json_to_text(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            input_data = await websocket.receive_json()
            await websocket.send_json(input_data)
    except WebSocketDisconnect:
        print("WebSocket disconnected")
