from websockets.sync.client import connect
import websockets
import asyncio
import ast


async def send_forward(websocket):
    input_data = ast.literal_eval(await websocket.recv())
    # await websocket.send(str(data))
    with connect("ws://localhost:8767") as target_websocket:
        target_websocket.send(str(input_data))
        # message = target_websocket.recv()
        # target_websocket.send(str({'name': 'Pavel', 'surname': 'Dolgy', 'age': 18}))
        response_data = target_websocket.recv()
        await websocket.send(f"Received: {response_data}")
    target_websocket.close()


start_server = websockets.serve(send_forward, "localhost", 8765)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
