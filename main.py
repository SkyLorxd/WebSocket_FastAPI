from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.websockets import WebSocket
from fastapi.encoders import jsonable_encoder
import asyncio
import websockets
import json


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


@app.websocket("/info")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        undefined_data = await websocket.receive()  # {"first_name": "Pavel", "second_name": "Dolgy", "age": 18}
        if isinstance(undefined_data, dict):
        # await websocket.send_text(undefined_data)
            uri = "ws://localhost:8765"
            async with websockets.connect(uri) as websocket_1:
                await websocket_1.send(str(undefined_data))
                data = await websocket_1.recv()
                await websocket.send(data)

        # await websocket.send_text(f"Your name is {data['name']}")
        # await websocket.send_text(f"Your surname is {data['surname']}")
        # await websocket.send_text(f"Your age is {data['age']}")


# async def send_txt():
#      uri = "ws://localhost:8765"
#      async with websockets.connect(uri) as websocket:
#          await websocket.send("text")
#          await websocket.recv()


# asyncio.get_event_loop().run_until_complete(send_txt())
