
'''
Sorts the users and messages by the given fields
and reindexes the files in that order.
'''


from load import *


def sort_users_by_id(users):
	def get_id(user):
		return user.id
	users = sorted(users, key=get_id)
	write_user_files(users)
	return users

def sort_users_by_state(users):
	def get_state(user):
		return user.state
	users = sorted(users, key=get_state)
	write_user_files(users)
	return users

def sort_messages_by_time(messages):
	def get_time(message):
		return (message.date.hour, message.date.minute)
	messages = sorted(messages, key=get_time)
	write_message_files(messages)
	return messages

def sort_messages_by_user(messages):
	def get_user(message):
		return message.user_id
	messages = sorted(messages, key=get_user)
	write_message_files(messages)
	return messages


def write_user_files(users):
	x = 0
	for user in users:
		write_user(user, x)
		x += 1

def write_message_files(messages):
	x = 0
	for message in messages:
		write_message(message, x)
		x += 1

