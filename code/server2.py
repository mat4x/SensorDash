#!/usr/bin/env python

import asyncio
import websockets
import socket
from base64 import b64decode
import wave
import json


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


hostname = socket.gethostname()
IPAddr = get_ip()
print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)
print(
    "* Enter {0}:5000 in the app.\n* Press the 'Set IP Address' button.\n* Select the sensors to stream.\n* Update the 'update interval' by entering a value in ms.".format(IPAddr))


async def echo(websocket, path):
    async for message in websocket:
        else:
            data = await websocket.recv()
            comps = json.loads(data)
            print(comps)
            

# Contribution by Evan Johnston
async def main():
    async with websockets.serve(echo, '0.0.0.0', 5000, max_size=1_000_000_000):
        await asyncio.Future()
    

asyncio.run(main())
