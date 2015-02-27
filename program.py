#!/usr/bin/python

import datetime
import time
import sys

from read_records import *


# Get the command line arguments. For the first and last records
# Calls the method to read all of the records from the dat files
# Loops through all the records and writes them to the csv files
# Finally, it prints out the total time that the operation takes

start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end = int(sys.argv[2]) if len(sys.argv) > 2 else start + 1

start_time = time.time()

records = read_all_records(start, end)

def pad_zeroes(number):
	number = str(number)
	while (len(number) < 6):
		number = "0" + number
	return number

count = 0
for record in records:
	id = pad_zeroes(record.id)
	user = open('csv/users/{0}.csv'.format(id), 'w')
	user.write(record.csv())
	print(record.csv())
	user.close()
	
	for message in record.messages:
		filename = 'csv/messages/{0}.csv'.format(pad_zeroes(count))
		message_file = open(filename, 'w')
		message_file.write(str(message.csv()))
		message_file.close()
		count = count + 1


total_time = time.time() - start_time

print('\nRead {0} records in {1} seconds\n'.format(len(records), total_time))


