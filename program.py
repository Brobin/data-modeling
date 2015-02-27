#!/usr/bin/python

import datetime
import time
import sys

from import_records import *
from sort_records import *


# Get the command line arguments for the corresponding functions
# Calls the method to read all of the records from the dat files
# Loops through all the records and writes them to the csv files
# Finally, it prints out the total time that the operation takes



length = len(sys.argv)

if length > 1:
	command = sys.argv[1]

	if command == "import":
		import_files()

	elif length > 2:
		arg = sys.argv[2]

		if command == "show":
			show_record(int(sys.argv[2]))

		elif command == "query":
			start_time = time.time()
			if arg == "1":
				users = load_users()
				print(len(nebraskans(users)))
			elif arg == "2":
				users = load_users_with_messages()
				print(len(early_birds(users)))
			elif arg == "3":
				users = load_users_with_messages()
				print(len(early_nebraskans(users)))
			elif arg == "4":
				users = load_users_with_messages()
				user = best_early_nebraskan(users)
				print(user)
				print(len(user.messages))
			total_time = time.time() - start_time
			print(total_time)

		else:
			print("second paramter required")
	else:
		error()
else:
	error()

def error():
	commands = [
		"\timport\timports binary files to csv\n",
		"\tquery\trun of the the queries (1-4)\n"
	]
	commands = ''.join([c for c in commands])
	print("\nPlease enter a command\n{0}".format(commands))
