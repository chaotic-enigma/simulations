from vpython import *
import time
import random

spaghatti = sphere(pos=vector(-1,0,0), color=color.cyan, radius=0.05)
benz = sphere(pos=vector(-2,0,0), color=color.green, radius=0.05)

for i in range(100):
	rate(10)
	print('spaghatti: {}, benz: {}'.format(spaghatti.pos.x, benz.pos.x))
	if spaghatti.pos.x <= 0.5900000000000009:
		spaghatti.pos.x += 0.03
		benz.pos.x += 0.03
	else:
		spaghatti.pos.x = spaghatti.pos.x
		benz.pos.x += 0.03
	time.sleep(0.2)