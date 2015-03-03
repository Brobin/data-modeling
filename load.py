
'''
Loads the data from the given records and rewrites
them into newly organized files.
'''


import datetime
import glob

from models import Message, User
from constants import *


def import_record(file, count):
	id, name, location, num = RECORD_USER.unpack(
		file.read(RECORD_USER.size))
	name = name.split(b"\0", 1)[0]
	location = location.split(b"\0", 1)[0]

	messages = []

	for x in range(0, num):
		message = import_message(file, id, count)
		messages.append(message)
		count = count + 1

	parts = location.split(",")
	names = name.split(" ", 2)
	record = User(id, names[0], names[1], parts[0], parts[1], messages)
	return (count, record)


def import_message(file, user_id, count):
	text, year, month, day, hour, minute = RECORD_MESSAGE.unpack(
		file.read(RECORD_MESSAGE.size))
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
		record  = open(RECORD_FILE.format(number), 'rb')
		count, processed_record = import_record(record, count)
		record.close()
		records.append(processed_record)
	return records


def pad_zeroes(number):
	number = str(number)
	while (len(number) < 6):
		number = "0" + number
	return number


def import_files():
	records = import_all_records(0, 2000)
	for user in records:
		write_user(user, user.id)
		for message in user.messages:
			write_message(message, message.id)


def write_user(user, number):
	number = pad_zeroes(number)
	user_file = open(USER_FILE.format(number), 'wb')
	user_file.write(user.byte())
	user_file.close()


def write_message(message, number):
	number = pad_zeroes(number)
	message_file = open(MESSAGE_FILE.format(number), 'wb')
	message_file.write(message.byte())
	message_file.close()


def load_users():
	users = []
	for user in glob.glob(USER_FILES):
		users.append(load_user(user))
	return users


def load_messages():
	messages = []
	for data in glob.glob(MESSAGE_FILES):
		message = load_message(data)
		messages.append(message)
	return messages


def load_message(filename):
	data = open(filename)
	id, user_id, year, month, day, hour, minute, text = MESSAGE_STRUCT.unpack(
		data.read(MESSAGE_STRUCT.size))
	data.close()
	date = datetime.datetime(year, month, day, hour, minute)
	message = Message(id, user_id, date, text)
	return message


def load_user(filename):
	data = open(filename)
	id, first, last, city, state = USER_STRUCT.unpack(
		data.read(USER_STRUCT.size))
	data.close()
	user = User(id, first, last, city, state)
	return user

