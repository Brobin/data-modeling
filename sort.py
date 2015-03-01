
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

def sort_users_by_state(users):
	def get_state(user):
		return user.state
	users = sorted(users, key=get_state)
	write_user_files(users)
	return users

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
	for user in users:
		write_user(user, user.id)

def write_message_files(messages):
	for message in messages:
		write_message(message, user.id)


