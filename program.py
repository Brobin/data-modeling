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

for record in records:
	id = str(record.id)
	while len(id) < 6:
		id = "0" + id

	user = open('csv/users/{0}.csv'.format(id), 'w')
	user.write(record.csv())
	print(record.csv())
	user.close()
	
	messages = open('csv/messages/{0}.csv'.format(id), 'w')
	for message in record.messages:
		messages.write("{0}\n".format(message.csv()))
	messages.close()


total_time = time.time() - start_time

print('\nRead {0} records in {1} seconds\n'.format(len(records), total_time))


