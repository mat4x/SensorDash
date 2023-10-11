import asyncio
import websockets
import socket
import json
import numpy

from tkinter import Tk, Label, Button

class ServerApp:
    def __init__(self):
        self.IP = self.get_ip()
        self.hostname = socket.gethostname()

        print(f"Name is:    {self.hostname}")
        print(f"IP Address: {self.IP}:5000")


    def get_ip(self):
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

    async def handler(self, websocket, path):
        async for message in websocket:
            message = await websocket.recv()
            data    = json.loads(message)
            #print(data)

            vals = (round( float( data['x'] ), 5 ),
                     round( float( data['y'] ), 5 ),
                     round( float( data['z'] ), 5 ) )

            x,y,z = vals

            print(f"{x:+.7f}  |  {y:+.7f}  |  {z:+.7f}")

            gui.update(vals)


    # Contribution by Evan Johnston
    async def start(self):
        async with websockets.serve(self.handler, '0.0.0.0', 5000, max_size=1_000_000_000):
            await asyncio.Future()


class GUIApp:
    def __init__(self, win):
        self.lbls = ( Label(win, text = 'X', font=(None, 30)),
                      Label(win, text = 'Y', font=(None, 30)),
                      Label(win, text = 'Z', font=(None, 30)) )

        self.lbls[0].place(relx=0.25, rely=0.5, anchor='center')
        self.lbls[1].place(relx=0.50, rely=0.5, anchor='center')
        self.lbls[2].place(relx=0.75, rely=0.5, anchor='center')

    def update(self, vals):
        for idx in range(3):
            n = min( 255, int(abs(vals[idx]) * 20) )
            color = (n,0,0) if vals[idx] < 0 else (0,n,0)
            self.lbls[idx].config(bg= "#%02x%02x%02x"%color)


def run_app():
    global gui
    win = Tk()
    gui = GUIApp(win)
    win.mainloop()


if __name__ == "__main__":
    import threading

    server = ServerApp()
    t1 = threading.Thread( target=lambda : asyncio.run(server.start()) )
    t1.start()

    t2 = threading.Thread( target=run_app )
    t2.start()    