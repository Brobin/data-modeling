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
from tree_user import *
from tree_query import *


def error():
	commands = [
		"\nload\t\tloads binary files to individual files\n",
		"users {field}\tsorts the users by a field\n\t\t(id, state)\n",
		"messages {field}\tsorts the messages by a field\n\t\t(time, user)\n",
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
		if arg == "time":
			sort_messages_by_time(messages)
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

	elif length > 3 and command == "tree-query":
		if sys.argv[2] == "1":
			users = load_users()
			build_user_tree(users, sys.argv[3])
			start_time = time.time()
			users = search_state('./users/tree/GROOOT_000000.dat', 'Nebraska')
			total = time.time() - start_time
			print(len(users))
			print(total)
	else:
		error()
else:
	error()
