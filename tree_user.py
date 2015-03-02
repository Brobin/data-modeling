
'''
Builds the data into a B+ tree on a given field

Node file contents - (starting value, ending value, list of filenames)
If node doesn't have children with data, set the values to null
list of filenames will be as long as the fanout

'''

import struct
import numpy
import glob


from sort import *
from load import load_users, pad_zeroes


def chunks(array, n):
	'''
	Splits a list into n-sized chunks
	'''
	chunks = []
	x = 0
	while x < len(array):
		num = min(len(array)-x, n)
		chunks.append(array[x:x+num])
		x += num
	return chunks


def build_user_tree(users, fanout):
	# sort the users
	users = sort_users_by_state(users)

	# get all the user files and make sure they're sorted
	user_files = glob.glob('./users/*.dat')
	user_files = sorted(user_files)

	# split the files and users into fanout sized chunks
	file_names = chunks(user_files, fanout)
	user_chunks = chunks(users, fanout)
	
	# get the first layer of the tree files
	layer = 0
	results = []
	for x in range(0, len(user_chunks)):
		results.append(write_user_node_initial(file_names[x], user_chunks[x], x, layer))

	# Loop until we create each layer down to the root
	layer = 1
	while len(results) > 1:
		result_chunks = chunks(results, fanout)
		results = []
		i = 0
		for chunk in result_chunks:
			files = []
			states = []
			for file, state in chunk:
				files.append(file)
				states.append(state)
			if len(result_chunks) < 2:
				# I AM GROOT!!!!!!!!!
				results.append(write_user_node(files, states, i, "GROOOT"))
			else:
				results.append(write_user_node(files, states, i, layer))
			i += 1
		layer += 1
	return results


def write_user_node_initial(files, users, name, layer):
	states = [u.state for u in users]
	return write_user_node(files, states, name, layer)


def write_user_node(files, states, name, layer):
	# set up the struct to pack the data correctly
	# num | filename | state | filename | state |filename
	s = struct.Struct('i' + '64s'*(len(files)) + '64s'*(len(states)-1))

	# open the file
	filename = './users/tree/{0}_{1}.dat'.format(pad_zeroes(layer), pad_zeroes(name))
	f = open(filename, 'wb')

	# prepare the data to pack
	output = []
	for x in range(0, len(files)):
		output.append(files[x])
		if x != len(states)-1:
			output.append(states[x])
	data = [len(files)+len(states)-1] + output

	# write the data
	f.write(s.pack(*data))
	return (filename, states[len(states)-1])


