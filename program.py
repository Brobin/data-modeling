#!/usr/bin/python

import datetime
import time
import sys

from query_tree import *
from query import *
from load import *
from sort import *


def error():
	commands = [
		"\tload\t\tloads binary files to individual files\n",
		"\tusers {field}\tsorts the users by a field\n",
		"\tquery {x}\trun of the the queries (1-4)\n"
	]
	commands = ''.join([c for c in commands])
	print("\nPlease enter a command\n{0}".format(commands))


length = len(sys.argv)

if length > 1:
	command = sys.argv[1]

	if command == "load":
		start_time = time.time()
		if length > 2 and sys.argv[2] == "tree":
			import_files()
			users = load_users()
			users = sort_users_by_id(users)
			construct_user_tree(users, 10)
			messages = load_messages()
			messages = sort_messages_by_id(messages)
			construct_message_tree(messages, 10)
		else:
			import_files()
		total_time = time.time() - start_time
		print(total_time)

	elif length > 2 and command == "users":
		start_time = time.time()
		arg = sys.argv[2]
		users = load_users()
		if arg == "id":
			users = sort_users_by_id(users)
		elif arg == "first":
			users = sort_users_by_first_name(users)
		elif arg == "last":
			users = sort_users_by_last_name(users)
		elif arg == "city":
			users = sort_users_by_city(users)
		elif arg == "state":
			users = sort_users_by_state(users)

		total_time = time.time() - start_time
		for user in users:
			print(user)
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
			print("invalid query: {0}".format(arg))
			error()
		total_time = time.time() - start_time
		print(total_time)
	else:
		error()
else:
	error()
