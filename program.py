#!/usr/bin/python

'''
This file contains the command line program logic to
run queries and set up the database.
'''

import datetime
import time
import sys

from query import *
from load import *
from sort import *


def error():
	commands = [
		"\nload\t\tloads binary files to individual files\n",
		"users {field}\tsorts the users by a field\n\t\t(id, first, last, city, state)\n",
		"messages {field}\tsorts the messages by a field\n\t\t(id, hour, user)\n",
		"query {x}\trun of the the queries (1-4)"
	]
	commands = ''.join([c for c in commands])
	print("Availiable Commands{0}".format(commands))


length = len(sys.argv)

if length > 1:
	command = sys.argv[1]

	if command == "load":
		start_time = time.time()
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
		else:
			print("ERROR: invalid query: {0}".format(arg))
			error()
		total_time = time.time() - start_time
		print(total_time)

	elif length > 2 and command == "messages":
		start_time = time.time()
		arg = sys.argv[2]
		messages = load_messages()
		if arg == "id":
			sort_messages_by_id(messages)
		elif arg == "hour":
			sort_messages_by_hour(messages)
		elif arg == "user":
			sort_messages_by_user(messages)
		else:
			print("ERROR: invalid query: {0}".format(arg))
			error()
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
			user, count = best_early_nebraskan(users)
			print(user)
			print(count)
		else:
			print("ERROR: invalid query: {0}".format(arg))
			error()
		total_time = time.time() - start_time
		print(total_time)
	else:
		error()
else:
	error()
