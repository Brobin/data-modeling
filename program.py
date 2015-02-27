#!/usr/bin/python

import datetime
import time
import sys

from import_records import *


# Get the command line arguments for the corresponding functions
# Calls the method to read all of the records from the dat files
# Loops through all the records and writes them to the csv files
# Finally, it prints out the total time that the operation takes

commands = [
	"\timport\timports binary files to csv\n",
	"\tshow\tshow a record\n"
]

length = len(sys.argv)

if length > 1:
	command = sys.argv[1]

	if command == "import":
		import_files()

	elif length > 2:
		arg = sys.argv[2]

		if command == "show":
			show_record(int(sys.argv[2]))

		elif command == "sort":
			if arg == "id":
				x = 5
				# sort by id
			elif arg == "name":
				x = 5
				# sort by name
			elif arg == "location":
				x = 5
				# sort by location
		else:
			print("second paramter required")
	else:
		commands = ''.join([c for c in commands])
		print("Please enter a command\n{0}".format(commands))

