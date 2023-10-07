import asyncio
import websockets
import socket
import json


class SensorApp:
    def __init__(self, handleEvent=lambda x: print(x)):
        self.handleEvent = handleEvent
        self.IP = self.get_ip()
        self.hostname    = socket.gethostname()

        print(f"Name is:    {self.hostname}")
        print(f"IP Address: {self.IP}:5000")


    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP


    async def handler(self, websocket, path):
        async for message in websocket:
            message = await websocket.recv()
            data    = json.loads(message)
            
            self.handleEvent(data)
    

    async def serve(self):
        async with websockets.serve(self.handler, '0.0.0.0', 5000, max_size=1_000_000_000) as socket:
            print(socket)
            await asyncio.Future()

    def start(self):
        asyncio.run(self.serve())


if __name__ == "__main__":
    server = SensorApp()
    asyncio.run(server.start())
