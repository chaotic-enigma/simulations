import time
import random
from vpython import *

tower = cone(pos=vector(0,-0.5,0), axis=vector(0,1.2,0), radius=0.1, color=color.green)
boundary = extrusion(pos=vector(0,-0.5,0), color=color.green, path=paths.ellipse(width=2.5, height=1.5),
	shape=shapes.ellipse(width=0.01, height=0.01), axis=vector(3,0,0))

blob1 = sphere(pos=vector(-4,2.5,0), radius=0.06, color=color.red)
blob2 = sphere(pos=vector(4,2.5,0), radius=0.06, color=color.orange, visible=False)
blob3 = sphere(pos=vector(-4,-2.5,0), radius=0.06, color=color.magenta, visible=False)
blob4 = sphere(pos=vector(4,-2.5,0), radius=0.06, color=color.yellow, visible=False)

for i in range(100):
	rate(10)
	print(blob1.pos.x, blob1.pos.y)
	# blob1.pos.x += 0.04
	# blob1.pos.y -= 0.03
	if blob1.pos.x <= -2.1199999999999983 and blob1.pos.y >= 1.0900000000000023:
		blob1.pos.x += 0.04
		blob1.pos.y -= 0.03
	else:
		blob1.pos.x += 0.05
		blob1.pos.y -= 0
		if blob1.pos.x == -1.2799999999999978:
			blob2.visible = True
			blob3.visible = True
		if blob1.pos.x == -1.1299999999999977:
			tower.color = color.white
			blob1.color = tower.color
			time.sleep(1.5)
			tower.color = color.green
			blob1.color = color.cyan
			break
	time.sleep(.25)
