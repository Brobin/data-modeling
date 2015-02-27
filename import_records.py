
import datetime
import struct
import time

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

	record = User(id, name, location, messages)
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
	for record in records:
		id = pad_zeroes(record.id)
		user = open('dat/users/{0}.dat'.format(id), 'wb')
		user.write(record.byte())
		user.close()
		
		for message in record.messages:
			name = pad_zeroes(message.id)
			message_file = open('dat/messages/{0}.dat'.format(name), 'wb')
			message_file.write(str(message.byte()))
			message_file.close()
	#users.close()

