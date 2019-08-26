from vpython import *
import time
import random

tower = cone(pos=vector(1.3,-1.1,0), axis=vector(0,1.2,0), radius=0.1, color=color.green)
boundary = extrusion(pos=vector(0.5,-1,0), color=color.green, path=paths.ellipse(width=2, height=1.5),
	shape=shapes.ellipse(width=0.01, height=0.01), axis=vector(2,0,0))
tcar = sphere(pos=vector(-3.5,-1,0),radius=0.06, color=color.red)

time.sleep(2)

i = -3.5
while i <= 0:
	rate(10)
	tcar.pos.x = i
	print(tcar.pos.x)
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
	print(secondcar.pos.x)
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

i = -3.5
while i <= -1.3400000000000016:
	rate(10)
	thirdcar.pos.x = i
	print(thirdcar.pos.x)
	if i == -2.150000000000002:
		thirdcar.color = secondcar.color
	i += 0.09
	time.sleep(.4)

time.sleep(1)

i = -0.08
while i <= 4:
	rate(10)
	tcar.pos.x = i
	print(tcar.pos.x)
	if i == 2.6199999999999997:
		tcar.color = color.red
		secondcar.color = color.green
		thirdcar.color = color.green
	if i == 3.9699999999999975:
		tcar.visible = False
		break
	i += 0.09
	time.sleep(.4)
