#!/usr/bin/python

import datetime
import time
import sys

from read_records import *

# Reads all the given records and puts them into
# csv files
def run_command(start, end):
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

# Get the command line arguments. 
# If two are provided, show the records that range
# Else, show the record of the first
start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end = int(sys.argv[2]) if len(sys.argv) > 2 else start + 1

run_command(start, end)


