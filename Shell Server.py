import os
import websockets
import asyncio

async def handle_command(command):
    result = os.system(command)
    print(result)

async def websocket_handler(websocket, path):
    if unsafe_mode == 1:
        print('New client accepted')
    else:
        accept_client = input('Accept a new client? (y/n): ')
        if accept_client.lower() != 'y':
            print('Client rejected')
            return
        else:
            print('New client accepted')
    
    async for message in websocket:
        await handle_command(message)

async def main():
    async with websockets.serve(websocket_handler, 'localhost', 8765):
        await asyncio.Future()

unsafe_mode = 0 #CHANGE THIS TO ENABLE UNSAFE MOD ALL CLIENTS WILL BE AUTOMAICLY ACCEPTED

asyncio.run(main())
