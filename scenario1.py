from vpython import *
import time
import random

tower = cone(pos=vector(1.3,-1.1,0), axis=vector(0,1.2,0), radius=0.1, color=color.green)
boundary = extrusion(pos=vector(0.5,-1,0), color=color.green, path=paths.ellipse(width=2, height=1.5),
	shape=shapes.ellipse(width=0.01, height=0.01), axis=vector(2,0,0))
tcar = sphere(pos=vector(-3.5,-1,0),radius=0.06, color=color.red)

time.sleep(5)

i = -3.5
while i <= 0:
	rate(10)
	tcar.pos.x = i
	# print(tcar.pos.x)
	if i == -1.5200000000000018:
		tcar.color = color.green
	i += 0.09
	time.sleep(.4)

time.sleep(0.5)
tcar.color = color.cyan
time.sleep(0.5)

secondcar = sphere(pos=vector(-3.5,-1,0), radius=0.06, color=color.orange)
time.sleep(1)

i = -3.5
while i <= 0:
	rate(10)
	secondcar.pos.x = i
	# print(secondcar.pos.x)
	if i == -1.5200000000000018:
		secondcar.color = color.cyan
	if i == -0.9800000000000014:
		tcar.color = color.white
		secondcar.color = color.white
		tower.color = color.white
		boundary.color = color.white
		break
	i += 0.09
	time.sleep(.4)

time.sleep(1)

tower.color = color.green
tcar.color = color.green
secondcar.color = color.cyan

thirdcar = sphere(pos=vector(-3.5,-1,0), radius=0.06, color=color.magenta)
time.sleep(1)

for i in range(100):
	rate(10)
	# print('thirdc : {} towerc : {}'.format(thirdcar.pos.x, tcar.pos.x))
	thirdcar.pos.x += 0.05
	tcar.pos.x += 0.09
	if tcar.pos.x == 1.5399999999999985:
		tower.color = color.white
		secondcar.color = color.white
		time.sleep(3)
	if thirdcar.pos.x == -2.100000000000005 and tcar.pos.x == 2.439999999999998:
		tcar.color = color.red
		# secondcar.color = color.white
		# tower.color = color.white
		time.sleep(2)
		secondcar.color = color.cyan
		thirdcar.color = color.cyan
	if tcar.pos.x == 3.159999999999997:
		tcar.visible = False
		boundary.visible = False
		break
	time.sleep(.4)

for i in range(100):
	rate(10)
	# print('secondc : {}'.format(secondcar.pos.x))
	secondcar.pos.x += 0.09
	if secondcar.pos.x < 1.8099999999999987:
		thirdcar.pos.x += 0.03
	if secondcar.pos.x == 1.8099999999999987:
		thirdcar.color = color.white
		thirdcar.pos.x = thirdcar.pos.x
	if secondcar.pos.x == 2.529999999999998:
		secondcar.color = color.orange
	if secondcar.pos.x >= 3.3399999999999967:
		secondcar.visible = False
		time.sleep(2)
		tower.color = color.green
		thirdcar.color = color.green
		break
	time.sleep(.4)
