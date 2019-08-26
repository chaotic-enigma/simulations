from vpython import *
import time
import random

tower = cone(pos=vector(0.7,-1.3,0), axis=vector(0,1.2,0), radius=0.1, color=color.green)

boundary = extrusion(pos=vector(0.5,-1,0), color=color.green, path=paths.ellipse(width=2, height=1.5),
	shape=shapes.ellipse(width=0.01, height=0.01), axis=vector(2,0,0))

tcar = sphere(pos=vector(-3.5,-1,0),radius=0.06, color=color.red)

for i in range(100):
	rate(10)
	tcar.pos.x += 0.05
	# print(tcar.pos.x)
	if tcar.pos.x == -1.5000000000000049:
		tcar.color = tower.color
	if tcar.pos.x == -0.6000000000000041:
		time.sleep(1.5)
		tower.color = color.white
		tcar.color = color.white
		time.sleep(1.5)
		tower.color = color.green
		tcar.color = color.cyan
	if tcar.pos.x == 0.04999999999999594:
		break
	time.sleep(.13)

time.sleep(1)

secondcar = sphere(pos=vector(-3.5,0.2,0), radius=0.06, color=color.orange)
time.sleep(1)

for i in range(100):
	rate(10)
	# print(secondcar.pos.x)
	secondcar.pos.x += 0.05
	if secondcar.pos.x == -0.9000000000000044:
		# time.sleep(1.5)
		secondcar.color = tcar.color
		time.sleep(1.5)
		tcar.color = tower.color
		break
	time.sleep(.13)

time.sleep(1)

thirdcar = sphere(pos=vector(-3.5,0.2,0), radius=0.06, color=color.magenta)
time.sleep(1)

for i in range(100):
	rate(10)
	thirdcar.pos.x += 0.02
	# print(thirdcar.pos.x)
	if thirdcar.pos.x == -2.359999999999999:
		time.sleep(1.5)
		thirdcar.color = secondcar.color
		break
	time.sleep(.13)

time.sleep(1)

for i in range(100):
	rate(10)
	secondcar.pos.x += 0.05
	thirdcar.pos.x += 0.02
	# print('second : {} ---- third : {}'.format(secondcar.pos.x, thirdcar.pos.x))
	if thirdcar.pos.x == -1.199999999999998:
		# time.sleep(1.5)
		tcar.color = color.white
		thirdcar.color = tcar.color
		time.sleep(1.5)
		tcar.color = color.cyan
		thirdcar.color = tcar.color
		time.sleep(1.5)
		tower.color = color.white
		secondcar.color = tower.color
		break
	time.sleep(.13)

time.sleep(1)
tower.color = color.green

for i in range(100):
	rate(10)
	secondcar.pos.x += 0.05
	thirdcar.pos.x += 0.03
	thirdcar.pos.y -= 0.04
	# print(thirdcar.pos.x)
	# if secondcar.pos.x == 2.8499999999999943:
	# 	thirdcar.pos.x += 0
	# 	thirdcar.pos.y -= 0
	if secondcar.pos.x == 3.249999999999993:
		secondcar.color = color.orange
		time.sleep(1.5)
		secondcar.visible = False
		break
	time.sleep(.13)
