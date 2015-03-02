
'''
Loads the data from the given records and rewrites
them into newly organized files.
'''


import datetime
import struct
import time
import glob

from models import Message, User


def import_record(file, count):
	RECORD = struct.Struct('i64s64si')
	id, name, location, num = RECORD.unpack(file.read(RECORD.size))
	name = name.split(b"\0", 1)[0]
	location = location.split(b"\0", 1)[0]

	messages = []

	for x in range(0, num):
		message = import_message(file, id, count)
		messages.append(message)
		count = count + 1

	parts = location.split(",")
	record = User(id, name, parts[0], parts[1], messages)
	return (count, record)

def import_message(file, user_id, count):
	MESSAGE = struct.Struct('1024siiiii')
	text, year, month, day, hour, minute = MESSAGE.unpack(file.read(MESSAGE.size))
	text = text.split(b"\0", 1)[0]
	date = datetime.datetime(year, month, day, hour, minute)
	message = Message(count, user_id, date, text)
	return message

def import_all_records(start, end):
	records = []
	count = 0
	for x in range(start, end):
		number = str(x)
		while(len(number) < 6):
			number = '0' + number
		record  = open('data/record_{0}.dat'.format(number), 'rb')
		count, processed_record = import_record(record, count)
		records.append(processed_record)
	return records

def pad_zeroes(number):
	number = str(number)
	while (len(number) < 6):
		number = "0" + number
	return number


def import_files():
	start_time = time.time()
	records = import_all_records(0, 2000)
	for user in records:
		write_user(user, user.id)
		for message in user.messages:
			write_message(message, message.id)

def write_user(user, number):
	number = pad_zeroes(number)
	user_file = open('./users/{0}.dat'.format(number), 'wb')
	user_file.write(user.byte())
	user_file.close()

def write_message(message, number):
	number = pad_zeroes(number)
	message_file = open('./messages/{0}.dat'.format(number), 'wb')
	message_file.write(message.byte())
	message_file.close()



USER_FILE = './users/*.dat'
MESSAGE_FILE = './messages/*.dat'

USER_STRUCT = 'i64s32s32s'
MESSAGE_STRUCT = 'iiiiiii1024s'

def load_users():
	users = []
	for user in glob.glob(USER_FILE):
		users.append(load_user(user))
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
		message = load_message(data)
		messages.append(message)	
	return messages

def load_message(filename):
	data = open(filename)
	load = struct.Struct(MESSAGE_STRUCT)
	id, user_id, year, month, day, hour, minute, text = load.unpack(data.read(load.size))
	date = datetime.datetime(year, month, day, hour, minute)
	message = Message(id, user_id, date, text)
	return message

def load_user(filename):
	data = open(filename)
	load = struct.Struct(USER_STRUCT)
	id, name, city, state = load.unpack(data.read(load.size))
	data.close()
	user = User(id, name, city, state)
	return user