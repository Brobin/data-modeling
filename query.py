
'''
This file contains functions to run queries against the flat
file system.
'''


import datetime
import struct
import time
import glob

from models import User, Message


def nebraskans(users):
	'''
	find all users from Nebraska.
	'''
	result = []
	for user in users:
		if "Nebraska" in user.state:
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
		print(user)
		num = 0
		for m in user.messages:
			if m.date.hour == 8 or (m.date.hour == 9 and m.date.minute == 0):
				num += 1
		if num > most_messages:
			most_messages = num
			best_user = user
	return (best_user, most_messages)

