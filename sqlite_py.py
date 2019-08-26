import sqlite3
import time
import datetime
import random
import math
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

conn = sqlite3.connect('pysqlite.db') # connect to database
c = conn.cursor() # same as cursor in the system that does things

# Execution is to do stuff

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS unknownData(unix REAL, datestamp TEXT, keyword TEXT, value REAL)") # cursor execution

def data_entry():
	c.execute("INSERT INTO unknownData VALUES(12427623, '2018-04-12', 'Python', 8)")
	conn.commit() # save
	c.close()
	conn.close()

def dynamic_data_entry():

	# variables
	unix = time.time() # record time
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = random.choice(['python','sql','data analysis','machine learning','deep learning','tensorflow','AI'])
	value = random.randrange(1,100)

	c.execute("INSERT INTO unknownData (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
		(unix, date, keyword, value)) # insert values

	conn.commit()

def read_from_db():
	c.execute("SELECT keyword, value, unix FROM unknownData WHERE keyword == 'AI' AND value > 43")
	entire_data = c.fetchall()
	for each_row in entire_data:
		print(each_row)

def graph_db():
	c.execute('SELECT unix, value FROM unknownData')
	data_graph = c.fetchall()

	dates = []
	points = []

	for row in data_graph:
		dates.append(datetime.datetime.fromtimestamp(row[0]))
		points.append(row[1])

	plt.plot_date(dates,points,'.-')
	plt.show()

def update_del_db():
	c.execute('SELECT * FROM unknownData')
	data = c.fetchall()
	al = [row for row in data]
	print(al)

	print('--------------------------------------------------------------------')

	c.execute('UPDATE unknownData SET value = 32 WHERE value = 324')
	conn.commit()

	c.execute('SELECT * FROM unknownData')
	data_up = c.fetchall()
	up = [row for row in data_up]
	print(up)

	print('--------------------------------------------------------------------')

	c.execute('SELECT * FROM unknownData WHERE value = 32')
	data_32 = c.fetchall()
	sele32 = [row for row in data_32]
	print(len(sele32))

	c.execute('DELETE FROM unknownData WHERE value = 32')
	conn.commit()

	c.execute('SELECT * FROM unknownData')
	del_data = c.fetchall()
	dele = [row for row in del_data]
	print(len(dele))
	print(dele)


'''
create_table()
#data_entry()
for i in range(20):
	dynamic_data_entry()
	time.sleep(1)

read_from_db()
'''
#update_del_db()

graph_db()

c.close()
conn.close()