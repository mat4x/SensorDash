import asyncio, websockets, socket, json

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

ACCO = 0
ORIN = 0

async def echo(websocket, path):
    global ACCO, ORIN
    async for message in websocket:
        data = await websocket.recv()
        comps = json.loads(data)
        print(comps)

        if comps['SensorName'] == 'Accelerometer':
            ACCO += 1
            print("ACCO:", ACCO)
        elif comps['SensorName'] == 'Orientation':
            ORIN += 1
            print("ORIN:", ORIN)
            

# Contribution by Evan Johnston
async def main():
    hostname = socket.gethostname()
    IPAddr   = get_ip()
    print(f"Your Computer Name is:       {hostname}")
    print(f"Your Computer IP Address is: {IPAddr}")
    async with websockets.serve(echo, '0.0.0.0', 5000, max_size=1_000_000_000):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())