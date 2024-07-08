from websockets.sync.client import connect
import websockets
import asyncio


async def send_forward(websocket):
    while True:
        input_data = await websocket.recv()
        with connect("ws://localhost:8767") as target_websocket:
            target_websocket.send(str(input_data))
            for i in range(3):
                received_data = target_websocket.recv()
                await websocket.send(f"Received: {received_data}")


async def main():
    async with websockets.serve(send_forward, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
