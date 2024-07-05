# from fastapi import FastAPI
# from fastapi.websockets import WebSocket
#
#
# app = FastAPI()
#
#
# @app.websocket("/")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_json()
#         await websocket.send_json(data)
#

import asyncio
import websockets


# async def get_json(websocket):
#     data = await websocket.recv()
#     await websocket.send(data)
#
#
# async def main():
#     async with websockets.serve(get_json, "localhost", 8765):
#         await asyncio.Future()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import websockets


async def fun(websocket):
    async for message in websocket:
        await websocket.send(f"This message '{message}' was processed by server")

    # uri = "ws://localhost:8000/info"
    # async with websockets.connect(uri) as websocket_1:
    #     data = await websocket_1.recv()
    #     await websocket_1.send(data)

start_server = websockets.serve(fun, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
