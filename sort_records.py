
import datetime
import time
import glob

from models import User, Message


def load_users():
	users = []
	for user_file in glob.glob('./csv/users/*.csv'):
		user_file = open(user_file)
		data = user_file.readline()
		data = data.split(";")
		user = User(int(data[0]), data[1], data[2])
		users.append(user)
	return users

def sort_users_by_id(users):
	def get_id(item):
		return item.id
	return sorted(users, key=get_id)

def load_users_with_messages():
	users = load_users()
	users = sort_users_by_id(users)
	messages = load_messages()
	for user in users:
		user.messages = [m for m in messages if m.user_id == user.id]
	return users

def load_messages():
	messages = []
	for message_file in glob.glob('./csv/messages/*.csv'):
		message_file = open(message_file)
		data = message_file.readline()
		data = data.split(";")
		date = date_parse(data[2])
		message = Message(int(data[0]), int(data[1]), date, data[3])
		messages.append(message)
		
	return messages

def date_parse(s):
	return datetime.datetime(int(s[0:4]),int(s[5:7]),
		int(s[8:10]), int(s[11:13]),
		int(s[14:16]), int(s[17:19]))


def nebraskans(users):
	'''
	find all users from Nebraska.
	'''
	result = []
	for user in users:
		if "Nebraska" in user.location:
			result.append(user)
	return result

def early_birds(users):
	'''
	find all users who sent messages between 8am-9am
	'''
	result = []
	for user in users:
		for message in user.messages:
			hour = message.date.hour
			minute = message.date.minute
			if hour == 8 or (hour == 9 and minute == 0):
				result.append(user)
				break
	return result

def early_nebraskans(users):
	'''
	find all users who sent messages between 8am-9am from Nebraska.
	'''
	return nebraskans(early_birds(users))

def best_early_nebraskan(users):
	'''
	find the user who sent the maximum number of messages 
	between 8am-9am from Nebraska
	'''
	users = early_nebraskans(users)
	best_user = None
	most_messages = 0
	for user in users:
		messages = len(user.messages)
		if messages > most_messages:
			most_messages = messages
			best_user = user
	return best_user

