
'''
Builds the data into a B+ tree on a given field
'''

from sort import *

def build_user_tree(users, field):
	if field == "id":
		users = sort_by_id(users)
	elif field == "first":
		users = sort_by_first_name(users)
	elif field == "last":
		users = sort_by_last_name(users)
	elif field == "city":
		users = sort_by_last_city(users)
	elif field == "state":
		users = sort_by_last_state(users)