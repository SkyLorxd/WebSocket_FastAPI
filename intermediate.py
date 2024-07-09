from fastapi import FastAPI, WebSocketDisconnect
from fastapi.websockets import WebSocket
from websocket import create_connection
import json


app = FastAPI()


@app.websocket("/")  # intermediate FastAPI server route
async def send_forward(current_websocket: WebSocket):
    await current_websocket.accept()
    target_websocket = create_connection("ws://127.0.0.1:3000/")
    try:
        input_data = await current_websocket.receive_json()
        target_websocket.send(json.dumps(input_data))
        for i in range(3):
            received_data = target_websocket.recv()
            await current_websocket.send_text(received_data)
        target_websocket.close()
    except WebSocketDisconnect:
        print("Client disconnected")
