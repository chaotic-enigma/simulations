import csv
import math
import time
import random
from vpython import *

scene.width = 1200
scene.height = 620

label(pos=vector(-30,15,0), text='Scenario 2', 
	color=color.cyan, box=False, height=20)
label(pos=vector(-30,13,0), text='strong - green\nmedium - orange\nweak - red', 
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

car_1 = sphere(pos=vector(3,15,0), radius=0.3, color=color.magenta)
car_2 = sphere(pos=vector(-3,-15,0), radius=0.3, color=color.magenta)

medium = 14
weak = 	18
strong = 7

tower_normal = color.white
medium_color = color.orange
weak_color = color.red
strong_color = color.green
not_reachable = color.magenta

print(dist(car_1, tower_1))
print(dist(car_1, tower_2))
print(dist(car_1, tower_3))
print(dist(car_1, tower_4))
print("\n")

print(dist(car_2, tower_1))
print(dist(car_2, tower_2))
print(dist(car_2, tower_3))
print(dist(car_2, tower_4))
print("\n")

dataset = [['car_id','pos_y','near_to','distance','signal_strength']]

time.sleep(4)

for i in range(1000):
	rate(10)
	car_1.pos.y -= 0.3
	car_2.pos.y += 0.3
	# print(car_1.pos.y, car_2.pos.y)
	if car_1.pos.y <= -15:
		break
	else:
		if dist(car_1, tower_3) <= strong:
			car_1.color = strong_color
			tower_3.color = strong_color
			dataset.append(['car_1',str(car_1.pos.y),'Tower-3',str(dist(car_1, tower_3)),'Strong'])
		if dist(car_2, tower_2) <= strong:
			car_2.color = strong_color
			tower_2.color = strong_color
			dataset.append(['car_2',str(car_2.pos.y),'Tower-2',str(dist(car_2, tower_2)),'Strong'])
		
		if strong < dist(car_1, tower_3) <= medium:
			car_1.color = medium_color
			tower_3.color = medium_color
			dataset.append(['car_1',str(car_1.pos.y),'Tower-3',str(dist(car_1, tower_3)),'Medium'])
		if strong < dist(car_2, tower_2) <= medium:
			car_2.color = medium_color
			tower_2.color = medium_color
			dataset.append(['car_2',str(car_2.pos.y),'Tower-2',str(dist(car_2, tower_2)),'Medium'])

		if medium < dist(car_1, tower_3) <= weak:
			car_1.color = weak_color
			tower_3.color = weak_color
			dataset.append(['car_1',str(car_1.pos.y),'Tower-3',str(dist(car_1, tower_3)),'Weak'])
			if dist(car_1, car_2) <= strong:
				car_1.color = strong_color
				car_2.color = strong_color
				dataset.append(['car_1',str(car_1.pos.y),'car_2',str(dist(car_1, car_2)),'Strong'])
			elif strong < dist(car_1, car_2) <= medium:
				car_1.color = medium_color
				car_2.color = medium_color
				dataset.append(['car_1',str(car_1.pos.y),'car_2',str(dist(car_1, car_2)),'Medium'])
			elif medium < dist(car_1, car_2) <= weak:
				car_1.color = weak_color
				car_2.color = weak_color
				dataset.append(['car_1',str(car_1.pos.y),'car_2',str(dist(car_1, car_2)),'Weak'])
			else:
				car_1.color = not_reachable
				car_2.color = not_reachable
		if medium < dist(car_2, tower_2) <= weak:
			car_2.color = weak_color
			tower_2.color = weak_color
			dataset.append(['car_2',str(car_2.pos.y),'Tower-2',str(dist(car_2, tower_2)),'Weak'])
			if dist(car_1, car_2) <= strong:
				tower_3.color = tower_2.color = tower_normal
				car_1.color = strong_color
				car_2.color = strong_color
				dataset.append(['car_2',str(car_2.pos.y),'car_1',str(dist(car_1, car_2)),'Strong'])
			# elif strong < dist(car_1, car_2) <= medium:
			# 	car_1.color = medium_color
			# 	car_2.color = medium_color
			# elif medium < dist(car_1, car_2) <= weak:
			# 	car_1.color = weak_color
			# 	car_2.color = weak_color
			else:
				car_1.color = not_reachable
				car_2.color = not_reachable
				tower_3.color = tower_normal
				tower_2.color = tower_normal
				# print(dist(car_2, tower_3))
				if dist(car_1, tower_2) <= strong:
					car_1.color = strong_color
					tower_2.color = strong_color
					dataset.append(['car_1',str(car_1.pos.y),'Tower-2',str(dist(car_1, tower_2)),'Strong'])
				if dist(car_2, tower_3) <= strong:
					car_2.color = strong_color
					tower_3.color = strong_color
					dataset.append(['car_2',str(car_2.pos.y),'Tower-3',str(dist(car_2, tower_3)),'Strong'])

				if strong < dist(car_1, tower_2) <= medium:
					car_1.color = medium_color
					tower_2.color = medium_color
					dataset.append(['car_1',str(car_1.pos.y),'Tower-2',str(dist(car_1, tower_2)),'Medium'])
				if strong < dist(car_2, tower_3) <= medium:
					car_2.color = medium_color
					tower_3.color = medium_color
					dataset.append(['car_2',str(car_2.pos.y),'Tower-3',str(dist(car_2, tower_3)),'Medium'])

				if medium < dist(car_1, tower_2) <= weak:
					car_1.color = weak_color
					tower_2.color = weak_color
					dataset.append(['car_1',str(car_1.pos.y),'Tower-2',str(dist(car_1, tower_2)),'Weak'])
				if medium < dist(car_2, tower_3) <= weak:
					car_2.color = weak_color
					tower_3.color = weak.color
					dataset.append(['car_2',str(car_2.pos.y),'Tower-3',str(dist(car_2, tower_3)),'Weak'])

	time.sleep(.08)
	
# print("\n")
# print(dist(tower_2, car_1))
# print(dataset)

with open('main_dis_scenario_2.csv', 'w') as dt:
	writer = csv.writer(dt)
	writer.writerows(dataset)

print('finished')