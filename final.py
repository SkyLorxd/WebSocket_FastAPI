import asyncio
import websockets
import ast


async def json_to_text(websocket):
    while True:
        input_data = ast.literal_eval(await websocket.recv())
        await websocket.send(f"Your name is {input_data['name']}")
        await websocket.send(f"Your surname is {input_data['surname']}")
        await websocket.send(f"You are {input_data['age']} years old")


async def main():
    async with websockets.serve(json_to_text, "localhost", 8767):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
