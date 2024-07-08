from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.websockets import WebSocket
import websockets

app = FastAPI()


@app.get("/")
def get_root():
    return PlainTextResponse("Hello world")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Your message: {data}")


@app.websocket("/info")  # main FastAPI servers route
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        input_data = await websocket.receive_json()  # {"name": "Pavel", "surname": "Dolgy", "age": 18}
        uri = "ws://localhost:8765"
        async with websockets.connect(uri) as intermediate_websocket:
            await intermediate_websocket.send(str(input_data))
            for i in range(3):
                received_data = await intermediate_websocket.recv()
                await websocket.send_text(str(received_data))
