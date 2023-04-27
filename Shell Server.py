import asyncio
import os
import websockets

async def handle_command(command):
    # Выполнить команду в консоли и получить результат
    result = os.system(command)
    print(result)

async def websocket_handler(websocket, path):
    async for message in websocket:
        # Обработать полученное сообщение как команду
        await handle_command(message)

async def main():
    async with websockets.serve(websocket_handler, 'localhost', 8765):
        await asyncio.Future()  # Ждем подключений

asyncio.run(main())
