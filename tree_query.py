
import struct

from load import load_message, load_user


def search_state(filename, key):
	'''
	Search all of the users and return the ones that are from the
	state provided (key)
	'''
	result = []

	# if the file is a leaf, add the user the result
	if "tree" not in filename:
		user = load_user(filename)
		if key in user.state:
			result.append(user)
	# else, the file is a root node
	else:
		# open the root file
		root = open(filename, 'rb')
		number = struct.unpack('i', root.read(4))[0]

		# extract all of the keys and pointers
		pointers = []
		keys = []
		for x in range(0, number-1, 2):
			pointers.append(struct.unpack('64s', root.read(64))[0].split('\x00',1)[0])
			keys.append(struct.unpack('64s', root.read(64))[0].split('\x00',1)[0])
		pointers.append(struct.unpack('64s', root.read(64))[0].split('\x00',1)[0])
		root.close()

		found = False
		for i in range(0, len(keys)):
			# if we haven't found a match yet and the current key is greater
			# than our search, add it to the result
			if not found and keys[i] > key:
				found = True
				result += search_state(pointers[i], key)
			# if the current key equals our search, add it to the result
			# if it is the last key, add the following pointer too
			elif keys[i] == key:
				result += search_state(pointers[i], key)
				if i == len(keys) - 1:
					result += search_state(pointers[i+1], key)
			# if we are on out last key and haven't found any matches yet,
			# search the last pointer
			elif i == len(keys) - 1 and not found:
				result += search_state(pointers[i+1], key)

	return result


def tree_time(filename, start_time, end_time):
	'''
	Search all of the messages and return the ones that were sent
	between the start and ending times.
	'''
	result = []
	if "tree" not in filename:
		message = load_message(filename)
		time = (message.date.hour, message.date.minute)
		if time >= start_time and time <= end_time:
			result.append(message)
	else:
		root = open(filename, 'rb')
		number = struct.unpack('i', root.read(4))[0]

		pointers = []
		times = []
		for x in range(0, number - 1, 2):
			pointers.append(struct.unpack('64s', root.read(64))[0].split('\x00',1)[0])
			times.append(struct.unpack('ii', root.read(8)))
		pointers.append(struct.unpack('64s', root.read(64))[0].split('\x00',1)[0])
		root.close()

		found = False
		for i in range(0, len(times)):

			if not found and times[i] > end_time:
				found = True
				result += tree_time(pointers[i], start_time, end_time)

			elif times[i] >= start_time and times[i] <= end_time:

				result += tree_time(pointers[i], start_time, end_time)
				if i == len(times) - 1:
					result += tree_time(pointers[i+1], start_time, end_time)

			elif i == len(times) - 1 and not found:
				result += tree_time(pointers[i+1], start_time, end_time)

	return result


def tree_nebraskans():
	'''
	Get all of the users that are from Nebraska
	'''
	user_root = './users/tree/GROOOT_000000.dat'
	users = search_state(user_root, 'Nebraska')
	return users

def tree_early_bird_messages():
	'''
	Get all of the messages sent between 8 and 9 am
	'''
	message_root = './messages/tree/GROOOT_000000.dat'
	messages = tree_time(message_root, (8,0), (9,0))
	return messages

def tree_early_birds():
	'''
	Get the user_ids of the users that sent messages
	between 8 and 9 am
	'''
	messages = tree_early_bird_messages()
	result = []
	for x in messages:
		if x.user_id not in result:
			result.append(x.user_id)
	return result

def tree_early_nebraskans():
	'''
	Get the users from Nebraska who sent messages
	between 8 and 9 am
	'''
	users = tree_nebraskans()
	ids = tree_early_birds()
	result = [u for u in users if u.id in ids]
	return result


def tree_best_early_nebraskan():
	'''
	Get the Nenbraskan who sent the most messages
	between 8 and 9 am
	'''
	users = tree_early_nebraskans()
	messages = tree_early_bird_messages()

	for user in users:
		user.messages = [m for m in messages if m.user_id == user.id]

	most_messages = 0
	best_user = None

	for user in users:
		m = len(user.messages)
		if m > most_messages:
			most_messages = m
			best_user = user

	return (best_user, most_messages)



