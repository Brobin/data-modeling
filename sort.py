
'''
Sorts the users and messages by the given fields
and reindexes the files in that order.
'''


from load import write_user, write_message


def sort_users_by_id(users):
	def get_id(user):
		return user.id
	users = sorted(users, key=get_id)
	write_user_files(users)
	return users

def sort_users_by_first_name(users):
	def get_first_name(user):
		return user.name.split(' ')[0]
	users = sorted(users, key=get_first_name)
	write_user_files(users)
	return users

def sort_users_by_last_name(users):
	def get_last_name(user):
		return user.name.split(' ')[1]
	users = sorted(users, key=get_last_name)
	write_user_files(users)
	return users

def sort_users_by_city(users):
	def get_city(user):
		return user.location.split(',')[0]
	users = sorted(users, key=get_city)
	write_user_files(users)
	return users

def sort_users_by_state(users):
	def get_state(user):
		return user.location.split(',')[1]
	users = sorted(users, key=get_state)
	write_user_files(users)
	return users


def sort_messages_by_id(messages):
	def get_id(message):
		return message.id
	messages = sorted(messages, key=get_id)
	write_message_files(messages)
	return messages

def sort_messages_by_hour(messages):
	def get_hour(message):
		return message.date.hour
	messages = sorted(messages, key=get_hour)
	write_message_files(messages)
	return messages

def sort_messages_by_user(messages):
	def get_user(message):
		return message.user_id
	messages = sorted(messages, key=get_user)
	write_message_files(messages)
	return messages


def write_user_files(users):
	count = 0
	for user in users:
		write_user(user, count)
		count = count + 1

def write_message_files(messages):
	count = 0
	for message in messages:
		write_message(message, count)
		count = count + 1


