import SensorClass
from threading import Thread
import time


READINGS_DATA = None

class DataGatherer:
    def __init__(self):
        self.file_name = f"{int(time.time())}.csv"


    def take_input(self):
        option = 1
        while option:
            print("Select train action [0 to exit]\n  1) Up\n  2) Down\n  3) Left\n  4) Right\n  5) STILL")
            option = int(input(": "))
            
            if not server.connected:
                print("Device not connected")
                continue

            if   (option == 1): self.record("UP")
            elif (option == 2): self.record("DOWN")
            elif (option == 3): self.record("LEFT")
            elif (option == 4): self.record("RIGHT")
            elif (option == 5): self.record("STILL")


    def record(self, action):
        global READINGS_DATA
        readings = []

        print("READY")
        time.sleep(2)
        for i in range(3, 0, -1):
            print(f"     {i}...")
            time.sleep(1)
        print("GO")

        t_end = time.time() + 1

        while time.time() < t_end:
            readings.append(READINGS_DATA)
            time.sleep(0.2)

        print(readings)
        with open(f".\\data\\{self.file_name}", 'a+') as file:
            for row in readings:
                file.write(','.join(str(val) for val in row) + f",{action}")
                file.write('\n')

        print(" Actions Recorded...")



def handler_fn(data):
    global READINGS_DATA
    READINGS_DATA = (float(data['x']),
                     float(data['z']) )


if __name__ == "__main__":
    server = SensorClass.SensorApp(handler_fn)
    gather = DataGatherer()

    thd_server = Thread(target = server.start)
    thd_gather = Thread(target = gather.take_input)

    thd_server.start()
    thd_gather.start()

    thd_server.join()
    thd_gather.join()
