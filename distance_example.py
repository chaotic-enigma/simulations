from vpython import *
import time
import math
import random
import csv

node_1 = sphere(pos=vector(-3.5,-1,0), radius=0.06, color=color.red)
node_2 = sphere(pos=vector(3.5,-1,0), radius=0.06, color=color.magenta)

def eucledian_distance(node1, node2):
	x1 = node1.pos.x
	x2 = node2.pos.x

	y1 = node1.pos.y
	y2 = node2.pos.y

	z1 = node1.pos.z
	z2 = node2.pos.z

	distance = math.sqrt( ((x1 - x2)**2) + ((y1 - y2)**2) + ((z1 - z2)**2) )

	return distance

# print(eucledian_distance(node_1, node_2))

strong = color.green
medium = color.cyan
weak = color.white

heading = ['nodes', 'signal_strength', 'distance']
data = [heading]

for i in range(1000):
	rate(10)
	node_1.pos.x += 0.09
	if eucledian_distance(node_1, node_2) <= 3:
		node_1.color = strong
		node_2.color = strong
		data.append(['node_1', 'strong', str(eucledian_distance(node_1, node_2))])
	if eucledian_distance(node_1, node_2) > 3 and eucledian_distance(node_1, node_2) <= 4:
		node_1.color = medium
		data.append(['node_1', 'medium', str(eucledian_distance(node_1, node_2))])
	if eucledian_distance(node_1, node_2) > 4:
		node_1.color = weak
		data.append(['node_1', 'weak', str(eucledian_distance(node_1, node_2))])
	# print(eucledian_distance(node_1, node_2))
	if eucledian_distance(node_1, node_2) == 1.1500000000000017:
		break
	time.sleep(.4)

with open('sample_data.csv', 'w') as dt:
	writer = csv.writer(dt)
	writer.writerows(data)

print('finished')
