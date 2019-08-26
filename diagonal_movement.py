import time
import random
from vpython import sphere, vector, color, rate

colorecolor = [color.red, color.orange, color.blue, color.green, color.white, color.magenta]

police_car = sphere(pos=vector(-3,2,0), color=color.cyan, radius=0.04)

while True:
	rate(10)
	police_car.color = random.choice(colorecolor)
	time.sleep(0.1)
	if police_car.pos.y >= -1.0499999999999976 and police_car.pos.x <= 3.099999999999995:
		police_car.pos.x += 0.05
		police_car.pos.y -= 0.025
		# print(police_car.pos.x)
	# time.sleep(0.05)