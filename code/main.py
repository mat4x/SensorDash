import SensorClass
import DashClass
import threading
import pygame as pg


class GyroSensorApp(SensorClass.SensorApp):
	def __init__(self, port_no, **kwarg):
		super().__init__(self.gyro_sensor_handler, port_no)
		self.__dict__.update(kwarg)

	
	def gyro_sensor_handler(self, data):
		x,y = float(data['z']), float(data['x'])
		
		if x > 5: 
			pg.event.post( pg.event.Event(pg.KEYDOWN, key=self.KEY_MAP["LEFT"]) )
			# print("LEFT")
		elif x < -5:
			pg.event.post( pg.event.Event(pg.KEYDOWN, key=self.KEY_MAP["RIGHT"]) )
			# print("RIGHT")

		if y > 5:  	
			pg.event.post( pg.event.Event(pg.KEYDOWN, key=self.KEY_MAP["UP"]) )
			# print("UP")
		elif y < -5:
			pg.event.post( pg.event.Event(pg.KEYDOWN, key=self.KEY_MAP["DOWN"]) )
			# print("DOWN")


KEY_MAP_LEFT  = {"LEFT"  : pg.K_a,
				 "RIGHT" : pg.K_d,
				 "UP"    : pg.K_w,
				 "DOWN"  : pg.K_s }

KEY_MAP_RIGHT = {"LEFT"  : pg.K_LEFT,
				 "RIGHT" : pg.K_RIGHT,
				 "UP"    : pg.K_UP,
				 "DOWN"  : pg.K_DOWN }


if __name__ == "__main__":
	pg.init()
	server_left  = GyroSensorApp(port_no = 5000, KEY_MAP = KEY_MAP_LEFT)
	server_right = GyroSensorApp(port_no = 5001, KEY_MAP = KEY_MAP_RIGHT)

	game = DashClass.GameApp()

	thd_server_left  = threading.Thread(target = server_left.start)
	thd_server_right = threading.Thread(target = server_right.start)

	thd_server_left.start()
	thd_server_right.start()

	game.start()

	thd_server_left.join()
	thd_server_right.join()
