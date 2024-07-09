# received_data = target_websocket.recv()
# await current_websocket.send_text(received_data)


# from fastapi import FastAPI, WebSocket
# from fastapi.websockets import WebSocket
# import fastapi.exceptions
# from fastapi.encoders import jsonable_encoder
# import asyncio
# import json
# import ast
# from contextlib import closing
# import websockets
# from fastapi.responses import PlainTextResponse
# import uvicorn
# from websockets.sync.client import connect
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


# async def fun(websocket):
#     async for message in websocket:
#
#         await websocket.send(f"This message '{message}' was processed by server")

    # uri = "ws://localhost:8000/info"
    # async with websockets.connect(uri) as websocket_1:
    #     data = await websocket_1.recv()
    #     await websocket_1.send(data)

# start_server = websockets.serve(fun, "localhost", 8765)
#
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

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

#
#
# app = FastAPI()
#
#
# @app.websocket("/")
# async def json_to_text(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         input_data = await websocket.receive_json()
#         with connect("ws://localhost:3000") as target_websocket:
#             target_websocket.send(input_data)
#             for i in range(3):
#                 received_data = target_websocket.recv()
#                 await websocket.send(received_data)
#
#
# async def send_forward(websocket):
#     while True:
#         input_data = await websocket.recv()
#         with connect("ws://localhost:3000") as target_websocket:
#             target_websocket.send(str(input_data))
#             for i in range(3):
#                 received_data = target_websocket.recv()
#                 await websocket.send(str(received_data))
#
#
# async def main():
#     async with websockets.serve(send_forward, "localhost", 2000):
#         await asyncio.Future()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

# if __name__ == "__main__":
#     uvicorn.run(app, port=3000)

#
# if __name__ == '__main__':
#     uvicorn.run("__main__:app", host="0.0.0.0", port=3000)
# async def main():
#     async with websockets.serve(json_to_text, "localhost", 8767):
#         await asyncio.Future()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())