'''
This file contains functions to run queries against the flat
file system.
'''

import datetime
import struct
import time
import glob

from models import User, Message

USER_FILE = './dat/users/*.dat'
MESSAGE_FILE = './dat/messages/*.dat'

USER_STRUCT = 'i64s64s'
MESSAGE_STRUCT = 'iiiiiii1024s'

def load_users():
	users = []
	load = struct.Struct(USER_STRUCT)
	for user in glob.glob(USER_FILE):
		data = open(user)
		id, name, location = load.unpack(data.read(load.size))
		user = User(id, name, location)
		users.append(user)
	return users


def load_users_with_messages():
	users = load_users()
	messages = load_messages()
	for m in messages:
		users[m.user_id].messages = users[m.user_id].messages + [m]
	return users

def load_messages():
	messages = []
	for data in glob.glob(MESSAGE_FILE):
		data = open(data)
		load = struct.Struct(MESSAGE_STRUCT)
		id, user_id, year, month, day, hour, minute, text = load.unpack(data.read(load.size))
		date = datetime.datetime(year, month, day, hour, minute)
		message = Message(id, user_id, date, text)
		messages.append(message)	
	return messages


def nebraskans(users):
	'''
	find all users from Nebraska.
	'''
	result = []
	for user in users:
		if "Nebraska" in user.location:
			result.append(user)
	return result

def early_birds(messages):
	'''
	find all users who sent messages between 8am-9am
	'''
	result = []
	for m in messages:
		hour = m.date.hour
		minute = m.date.minute
		if hour == 8 or (hour == 9 and minute == 0):
			if m.user_id not in result:
				result.append(m.user_id)
	return result

def early_nebraskans(users, messages):
	'''
	find all users who sent messages between 8am-9am from Nebraska.
	'''
	users = nebraskans(users)
	ids = early_birds(messages)
	users = [u for u in users if u.id in ids]
	return users

def best_early_nebraskan(users):
	'''
	find the user who sent the maximum number of messages 
	between 8am-9am from Nebraska
	'''
	messages = []
	for user in users:
		messages = messages + user.messages
	users = early_nebraskans(users, messages)
	best_user = None
	most_messages = 0
	for user in users:
		messages = len(user.messages)
		if messages > most_messages:
			most_messages = messages
			best_user = user
	return best_user

