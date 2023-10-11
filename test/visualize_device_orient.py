import asyncio, websockets, socket, json, numpy
import threading as thd

from tkinter import Tk, Label

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

ORIN = (0,0,0)

async def echo(websocket, path):
    global ORIN
    async for message in websocket:
        data = await websocket.recv()
        comps = json.loads(data)
            
        ORIN = ( float(comps['azimuth']),
                 float(comps['pitch']),
                 float(comps['roll']) )

        print( f"{ORIN[0]:0.5f}   {ORIN[1]:0.2f}   {ORIN[2]:0.2f}")

        l1.config( bg = get_color(ORIN[0]) )
        l2.config( bg = get_color(ORIN[1]) )
        l3.config( bg = get_color(ORIN[2]) )
            

# Contribution by Evan Johnston
async def main():
    hostname = socket.gethostname()
    IPAddr   = get_ip()
    print(f"Your Computer Name is:       {hostname}")
    print(f"Your Computer IP Address is: {IPAddr}")
    async with websockets.serve(echo, '0.0.0.0', 5000, max_size=1_000_000_000):
        await asyncio.Future()


def get_color(val):
    val = val - 180
    n = int((180-abs(val))/180 * 254)
    color = (n,0,0) if val>0 else (0,0,n)
    return "#%02x%02x%02x" % color

def GUI():
    global l1, l2, l3
    win = Tk()
    l1  = Label(win, fg='white', text="azimuth", font=(None, 30))
    l1.place(relx=0.25, rely=0.5, anchor='center')
    
    l2  = Label(win, fg='white', text="pitch"  , font=(None, 30))
    l2.place(relx=0.5,  rely=0.5, anchor='center')
    
    l3  = Label(win, fg='white', text="roll"   , font=(None, 30))
    l3.place(relx=0.75, rely=0.5, anchor='center')

    win.mainloop()

if __name__ == "__main__":
    t1 = thd.Thread(target = lambda: asyncio.run(main()))
    t1.start()

    t2 = thd.Thread(target = GUI)
    t2.start()

    t1.join()
    t2.join()