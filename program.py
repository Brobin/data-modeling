#!/usr/bin/python

import datetime
import time
import sys

from import_records import *
from sort_records import *


length = len(sys.argv)

if length > 1:
	command = sys.argv[1]

	if command == "import":
		start_time = time.time()
		import_files()
		total_time = time.time() - start_time
		print(total_time)

	elif length > 2 and command == "query":
		arg = sys.argv[2]
		start_time = time.time()
		if arg == "1":
			users = load_users()
			print(len(nebraskans(users)))
		elif arg == "2":
			messages = load_messages()
			print(len(early_birds(messages)))
		elif arg == "3":
			users = load_users()
			messages = load_messages()
			print(len(early_nebraskans(users, messages)))
		elif arg == "4":
			users = load_users_with_messages()
			user = best_early_nebraskan(users)
			print(user)
			print(len(user.messages))
		else:
			print("invalid query")
		total_time = time.time() - start_time
		print(total_time)
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
