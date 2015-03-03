
'''
This file contains functions to run queries against the flat
file system.
'''


from models import User, Message
from load import load_users, load_messages


def nebraskans():
	'''
	find all users from Nebraska.
	'''
	users = load_users()
	result = []
	for user in users:
		if "Nebraska" in user.state:
			result.append(user)
	return result

def early_messages():
	messages = load_messages()
	result = []
	for m in messages:
		hour = m.date.hour
		minute = m.date.minute
		time = (hour, minute)
		if time >= (8,0) and time <= (9,0):
			result.append(m)
	return result

def early_birds():
	'''
	find all users who sent messages between 8am-9am
	'''
	messages = early_messages()
	result = []
	for m in messages:
		if m.user_id not in result:
			result.append(m.user_id)
	return result

def early_nebraskans():
	'''
	find all users who sent messages between 8am-9am from Nebraska.
	'''
	users = nebraskans()
	ids = early_birds()
	users = [u for u in users if u.id in ids]
	return users

def best_early_nebraskan():
	'''
	find the user who sent the maximum number of messages 
	between 8am-9am from Nebraska
	'''
	users = early_nebraskans()
	messages = early_messages()

	best_user = None
	most_messages = 0
	for user in users:
		user.messages = [m for m in messages if m.user_id == user.id]
		if len(user.messages) > most_messages:
			most_messages = len(user.messages)
			best_user = user
	return (best_user, most_messages)

