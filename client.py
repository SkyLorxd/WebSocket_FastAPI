import aiohttp
from aiohttp.http_websocket import WSMessage
import asyncio


async def handler():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("ws://127.0.0.1:1000/") as websocket:
            await websocket.send_json({"name": "Pavel", "surname": "Dolgy", "age": 18})
            async for message in websocket:
                if isinstance(message, WSMessage):
                    resp = message.data
                    print("Получен ответ от сервера:", resp)
            if not websocket.closed:
                await websocket.close()


asyncio.run(handler())


