
'''
Builds the data into a B+ tree on a given field
'''

from sort import *

def build_user_tree(users, field, fanout):
	if field == "id":
		users = sort_by_id(users)
	elif field == "state":
		users = sort_by_last_state(users)

