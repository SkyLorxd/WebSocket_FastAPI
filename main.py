from fastapi import FastAPI, WebSocketDisconnect
from fastapi.websockets import WebSocket
from websocket import create_connection
import json


app = FastAPI()


@app.websocket("/")  # main FastAPI servers route
async def websocket_endpoint(current_websocket: WebSocket):
    await current_websocket.accept()
    intermediate_websocket = create_connection("ws://127.0.0.1:2000/")
    try:
        while True:
            input_data = await current_websocket.receive_json()  # {"name": "Pavel", "surname": "Dolgy", "age": 18}
            intermediate_websocket.send(json.dumps(input_data))
            for i in range(3):
                received_data = intermediate_websocket.recv()
                await current_websocket.send_text(received_data)
    except WebSocketDisconnect:
        print("WebSocket disconnected")
