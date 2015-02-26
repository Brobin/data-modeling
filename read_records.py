
import datetime
import struct

from models import Message, User


def read_record(file):
	RECORD = struct.Struct('i64s64si')
	id, name, location, num = RECORD.unpack(file.read(RECORD.size))
	name = name.split(b"\0", 1)[0]
	location = location.split(b"\0", 1)[0]

	messages = []

	for x in range(0, num):
		message = read_message(file, id)
		messages.append(message)

	record = User(id, name, location, messages)
	return record


def read_message(file, user_id):
	MESSAGE = struct.Struct('1024siiiii')
	text, year, month, day, hour, minute = MESSAGE.unpack(file.read(MESSAGE.size))
	text = text.split(b"\0", 1)[0]
	date = datetime.datetime(year, month, day, hour, minute)
	message = Message(date, text, user_id)
	return message


def read_all_records(start, end):
	records = []

	for x in range(start, end):
		number = str(x)
		while(len(number) < 6):
			number = '0' + number
		record  = open('data/record_{0}.dat'.format(number), 'rb')
		processed_record = read_record(record)
		records.append(processed_record)
	return records

