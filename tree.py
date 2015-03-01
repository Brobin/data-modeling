
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
		results.append(write_tree_file_initial(file_names[x], user_chunks[x], x, layer))

	layer = 1
	# loop until we create each layer until the root
	while len(results) > 1:

		# chunk it into fanout sized pieces
		result_chunks = chunks(results, fanout)
		results = []
		i = 0
		# go through each result
		for x in result_chunks:
			files = []
			beg = x[0][1]
			end = x[len(x)-1][2]
			# add each result to the files to write
			for y in x:
				files.append(y[0])

			# write the tree file
			if len(results) == 0:
				results.append(write_file(files, beg, end, i, "ROOOOT"))
			else:
				results.append(write_file(files, beg, end, i, layer))
			i += 1
		layer += 1

	return results



def write_tree_file_initial(files, users, name, layer):
	beg_state = users[0].state.split('\x00', 1)[0]
	end_state = users[len(users)-1].state.split('\x00', 1)[0]
	return write_file(files, beg_state, end_state, name, layer)


def write_file(files, beg_state, end_state, name, layer):
	s = struct.Struct('32s32si' + '64s'*len(files))
	filename = './users/tree/tree_{0}_{1}.dat'.format(pad_zeroes(layer), pad_zeroes(name))
	f = open(filename, 'wb')
	data = [beg_state, end_state, len(files)-1] + [x for x in files]
	f.write(s.pack(*data))
	return (filename, beg_state, end_state)


def chunks(array, n):
	chunks = []
	x = 0
	while x < len(array):
		num = min(len(array)-x, n)
		chunks.append(array[x:x+num])
		x += num
	return chunks

result = build_user_tree(load_users(), 200)
print(result)

