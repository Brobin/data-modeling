'''
This file contains functions to query against the
file system organized in B+ trees
'''

import datetime
import shutil
import struct
import time
import os

from models import User, Message
from query import load_users, load_messages
from sort import *

def pad_zeroes(number):
	number = str(number)
	while (len(number) < 6):
		number = "0" + number
	return number

def construct_file_tree(objects, fanout, directory):
	layer = 0
	count = 0
	children = 10
	objects_left = len(objects) - 1
	for x in range(0, len(objects)):
		if count >= fanout ** layer:
			layer = layer + 1
			count = 0

		if objects_left > fanout:
			children = fanout
		else:
			children = objects_left % fanout

		object = objects[x]
		name = '{0}/{1}_{2}_{3}.dat'.format(directory, pad_zeroes(layer),
			pad_zeroes(count), pad_zeroes(children))

		object_file = open(name, 'wb')
		object_file.write(object.byte())

		count = count + 1
		objects_left = objects_left - children


def construct_message_tree(messages, fanout):
	construct_file_tree(messages, fanout, './tree/messages')


def construct_user_tree(users, fanout):
	construct_file_tree(users, fanout, './tree/users')

