
def sort_users_by_id(users):
	def get_id(item):
		return item.id
	return sorted(users, key=get_id)

def sort_users_by_first_name(users):
	def get_first_name(item):
		return item.name.split(' ')[0]
	return sorted(users, key=get_first_name)

def sort_users_by_last_name(users):
	def get_last_name(item):
		return item.name.split(' ')[1]
	return sorted(users, key=get_last_name)

def sort_users_by_city(users):
	def get_city(item):
		return item.location.split(',')[0]
	return sorted(users, key=get_city)

def sort_users_by_state(users):
	def get_state(item):
		return item.location.split(',')[1]
	return sorted(users, key=get_state)


def sort_messages_by_date(messages):
	def get_date(item):
		return item.date
	return sorted(users, key=get_date)

def sort_messages_by_user(messages):
	def get_user(item):
		return item.user_id
	return sorted(messages, key=get_user)
