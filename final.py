import asyncio
import websockets
import ast


async def json_to_text(websocket):
    async for message in websocket:
        # data = ast.literal_eval(await websocket.recv())  # {"first_name": "Pavel", "second_name": "Dolgy", "age": 18}
        await websocket.send(f"Your name is {ast.literal_eval(message)['name']}")
        await websocket.send(f"Your surname is {ast.literal_eval(message)['surname']}")
        # await websocket.send(f"Your age is {ast.literal_eval(message)['age']}")


async def main():
    async with websockets.serve(json_to_text, "localhost", 8767):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
