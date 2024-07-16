import asyncio
import websockets


async def receive_send(websocket):
    async for message in websocket:
        async with websockets.connect('ws://localhost:3000') as target_websocket:
            await target_websocket.send(message)
            async for response in target_websocket:
                await websocket.send(response)


async def main():
    server = await websockets.serve(receive_send, "localhost", 2000)
    await server.wait_closed()

asyncio.run(main())
