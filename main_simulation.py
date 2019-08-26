import csv
import math
import time
import random
from vpython import *

scene.width = 1200
scene.height = 620

label(pos=vector(-30,18,0), text='Scenario 1', 
	color=color.cyan, box=False, height=20)
label(pos=vector(-30,16,0), text='strong - green\nmedium - orange\nweak - red', 
	depth=0, color=color.cyan)

label(pos=vector(-32,3,0), text='Tower 1', color=color.yellow, depth=0)
tower_1 = arrow(pos=vector(-30,5,-2), axis=vector(0,2,0), 
	color=color.white, shaftwidth=0.7)

label(pos=vector(-12,-11,0), text='Tower 2', color=color.yellow, depth=0)
tower_2 = arrow(pos=vector(-10,-10,-2), axis=vector(0,2,0), 
	color=color.white, shaftwidth=0.7)

label(pos=vector(13,8,0), text='Tower 3', color=color.yellow, depth=0)
tower_3 = arrow(pos=vector(15,10,-2), axis=vector(0,2,0), 
	color=color.white, shaftwidth=0.7)

label(pos=vector(28,0,0), text='Tower 4', color=color.yellow, depth=0)
tower_4 = arrow(pos=vector(30,1,-2), axis=vector(0,2,0), 
	color=color.white, shaftwidth=0.7)

def dist(node1, node2):
	x1 = node1.pos.x
	x2 = node2.pos.x

	y1 = node1.pos.y
	y2 = node2.pos.y

	z1 = node1.pos.z
	z2 = node2.pos.z

	distance = math.sqrt( ((x1 - x2)**2) + ((y1 - y2)**2) + ((z1 - z2)**2) )

	return distance

car_1 = sphere(pos=vector(-35,-3,0), radius=0.3, color=color.magenta)

medium = 10
weak = 	15
strong = 6

medium_color = color.orange
weak_color = color.red
strong_color = color.green

time.sleep(5)

data = [['cars','pos_x','near_to','distance','signal_strength']]

for i in  range(1000):
	rate(10)
	car_1.pos.x += 0.3
	if car_1.pos.x >= 36:
		break
	else:
		if (dist(car_1, tower_1) < dist(car_1, tower_2)) and (dist(car_1, tower_1) < dist(car_1, tower_3)) and (dist(car_1, tower_1) < dist(car_1, tower_4)):
			if dist(car_1, tower_1) <= strong:
				tower_1.color = strong_color
				car_1.color = strong_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-1',str(dist(car_1, tower_1)),'Strong'])
			elif strong < dist(car_1, tower_1) <= medium:
				tower_1.color = medium_color
				car_1.color = medium_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-1',str(dist(car_1, tower_1)),'Medium'])
			elif medium < dist(car_1, tower_1) <= weak:
				tower_1.color = weak_color
				car_1.color = weak_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-1',str(dist(car_1, tower_1)),'Weak'])
			else:
				tower_1.color = color.white
				car_1.color = color.magenta
		elif (dist(car_1, tower_2) < dist(car_1, tower_1)) and (dist(car_1, tower_2) < dist(car_1, tower_3)) and (dist(car_1, tower_2) < dist(car_1, tower_4)):
			tower_1.color = color.white
			car_1.color = tower_1.color
			if dist(car_1, tower_2) <= strong:
				tower_2.color = strong_color
				car_1.color = strong_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-2',str(dist(car_1, tower_2)),'Strong'])
			elif strong < dist(car_1, tower_2) <= medium:
				tower_2.color = medium_color
				car_1.color = medium_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-2',str(dist(car_1, tower_2)),'Medium'])
			elif medium < dist(car_1, tower_2) <= weak:
				tower_2.color = weak_color
				car_1.color = weak_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-2',str(dist(car_1, tower_2)),'Weak'])
			else:
				tower_2.color = color.white
				car_1.color = tower_2.color
		elif (dist(car_1, tower_3) < dist(car_1, tower_1)) and (dist(car_1, tower_3) < dist(car_1, tower_2)) and (dist(car_1, tower_3) < dist(car_1, tower_4)):
			tower_2.color = color.white
			car_1.color = color.magenta
			if dist(car_1, tower_3) <= strong:
				tower_3.color = strong_color
				car_1.color = strong_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-3',str(dist(car_1, tower_3)),'Strong'])
			elif strong < dist(car_1, tower_3) <= medium:
				tower_3.color = medium_color
				car_1.color = medium_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-3',str(dist(car_1, tower_3)),'Medium'])
			elif medium < dist(car_1, tower_3) <= weak:
				tower_3.color = weak_color
				car_1.color = weak_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-3',str(dist(car_1, tower_3)),'Weak'])
			else:
				tower_3.color = color.white
				car_1.color = color.magenta
		elif (dist(car_1, tower_4) < dist(car_1, tower_1)) and (dist(car_1, tower_4) < dist(car_1, tower_2)) and (dist(car_1, tower_4) < dist(car_1, tower_3)):
			tower_3.color = color.white
			car_1.color = tower_3.color
			if dist(car_1, tower_4) <= strong:
				tower_4.color = strong_color
				car_1.color = strong_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-4',str(dist(car_1, tower_4)),'Strong'])
			elif strong < dist(car_1, tower_4) <= medium:
				tower_4.color = medium_color
				car_1.color = medium_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-4',str(dist(car_1, tower_4)),'Medium'])
			elif medium < dist(car_1, tower_4) <= weak:
				tower_4.color = weak_color
				car_1.color = weak_color
				data.append(['Car-1',str(car_1.pos.x),'Tower-4',str(dist(car_1, tower_4)),'Weak'])
			else:
				tower_4.color = color.white
				car_1.color = color.magenta

	time.sleep(.04)

with open('main_dis_scenario_1.csv', 'w') as dt:
	writer = csv.writer(dt)
	writer.writerows(data)

print('finished')