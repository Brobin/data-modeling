
import datetime
import struct
import time

from models import Message, User


def import_record(file):
	count = 0
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
	return record


def import_message(file, user_id, count):
	MESSAGE = struct.Struct('1024siiiii')
	text, year, month, day, hour, minute = MESSAGE.unpack(file.read(MESSAGE.size))
	text = text.split(b"\0", 1)[0]
	date = datetime.datetime(year, month, day, hour, minute)
	message = Message(count, user_id, date, text)
	return message


def import_all_records(start, end):
	records = []

	for x in range(start, end):
		number = str(x)
		while(len(number) < 6):
			number = '0' + number
		record  = open('data/record_{0}.dat'.format(number), 'rb')
		processed_record = import_record(record)
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
	count = 0

	for record in records:
		id = pad_zeroes(record.id)
		user = open('csv/users/{0}.csv'.format(id), 'w')
		user.write(record.csv())
		user.close()
		
		for message in record.messages:
			name = pad_zeroes(count)
			filename = 'csv/messages/{0}.csv'.format(name)
			message_file = open(filename, 'w')
			message_file.write(str(count) + ";" + str(message.csv()))
			message_file.close()
			count = count + 1


	total_time = time.time() - start_time

	print('\nRead {0} records in {1} seconds\n'
		.format(len(records), total_time))

