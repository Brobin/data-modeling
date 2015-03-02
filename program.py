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
from tree_user import build_user_tree
from tree_message import build_message_tree
from tree_query import *


def error():
	commands = [
		"\nload\t\tloads binary files to individual files\n",
		"tree {fnout}\tbuilds the B+ trees of users and messages\n",
		"query {x}\trun of the the queries (1-4)\n",
		"tree_query {x}\trun the query on the B+ tree (1-4)\n"
	]
	commands = ''.join([c for c in commands])
	print("\nAvailiable Commands{0}".format(commands))


length = len(sys.argv)

if length > 1:
	command = sys.argv[1]

	if command == "load":
		start_time = time.time()
		import_files()
		total_time = time.time() - start_time
		print("\nImported messages and users in {0}\n".format(total_time))

	elif length > 2 and command == "tree":
		fanout = int(sys.argv[2])

		start = time.time()
		users = load_users()
		build_user_tree(users, fanout)
		end = time.time() - start
		print("\nBuilt user B+ tree of fanout {0} in {1} seconds".format(fanout, end))

		start = time.time()
		messages = load_messages()
		build_message_tree(messages, fanout)
		end = time.time() - start
		print("Built message B+ tree of fanout {0} in {1} seconds\n".format(fanout, end))

	elif length > 2 and command == "query":
		arg = sys.argv[2]
		start_time = time.time()
		if arg == "1":
			print(len(nebraskans()))
		elif arg == "2":
			print(len(early_birds()))
		elif arg == "3":
			print(len(early_nebraskans()))
		elif arg == "4":
			user, count = best_early_nebraskan()
			print(user)
			print(count)
		else:
			print("ERROR: invalid query: {0}".format(arg))
			error()
		total_time = time.time() - start_time
		print(total_time)

	elif length > 2 and command == "tree-query":
		arg = sys.argv[2]
		start = time.time()
		if arg == "1":
			users = tree_nebraskans()
			print(len(users))
		elif arg == "2":
			result = tree_early_birds()
			print(len(result))
		elif arg == "3":
			result = tree_early_nebraskans()
			print(len(result))
		elif arg == "4":
			user, messages = tree_best_early_nebraskan()
			print(user)
			print(messages)
		total = time.time() - start
		print(total)
	else:
		error()
else:
	error()
