from fastapi import FastAPI, WebSocketDisconnect
from fastapi.websockets import WebSocket


app = FastAPI()


@app.websocket("/")  # final FastAPI server route
async def json_to_text(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            input_data = await websocket.receive_json()
            await websocket.send_text(f"Your name is {input_data['name']}")
            await websocket.send_text(f"Your surname is {input_data['surname']}")
            await websocket.send_text(f"You are {input_data['age']} years old")
    except WebSocketDisconnect:
        print("WebSocket disconnected")
