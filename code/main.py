import SensorClass
import DashClass
import threading
import pygame as pg


if __name__ == "__main__":
	pg.init()

	server1 = SensorClass.SensorApp(port_no = 5000)
	server2 = SensorClass.SensorApp(port_no = 5001)

	game = DashClass.GameApp()



	thd_server1 = threading.Thread(target = server1.start)
	thd_server2 = threading.Thread(target = server2.start)

	thd_server1.start()
	thd_server2.start()

	game.start()

	thd_server1.join()
	thd_server2.join()