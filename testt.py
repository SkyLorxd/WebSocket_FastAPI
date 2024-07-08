# from fastapi import FastAPI
# from fastapi.websockets import WebSocket
# import fastapi.exceptions
# from fastapi.encoders import jsonable_encoder
# import asyncio
# import json
# import ast
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

        # await websocket.send_text(str(undefined_data))
        # if isinstance(undefined_data, dict):
        # await websocket.send_text(undefined_data)
        # try:
        # except  WebSocketDisconnect:
        #     await websocket.send_text("The connection was closed for some reason")
        # await websocket.send_text(f"Your name is {data['name']}")
        # await websocket.send_text(f"Your surname is {data['surname']}")
        # await websocket.send_text(f"Your age is {data['age']}")


# async def send_txt():
#      uri = "ws://localhost:8765"
#      async with websockets.connect(uri) as websocket:
#          await websocket.send("text")
#          await websocket.recv()


# asyncio.get_event_loop().run_until_complete(send_txt())

# target_websocket.close()
# async for message in websocket:
# data = ast.literal_eval(await websocket.recv())  # {"first_name": "Pavel", "second_name": "Dolgy", "age": 18}