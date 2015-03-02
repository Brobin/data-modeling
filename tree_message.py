
'''
builds the Messages B+ tree sorted by the time (hour, minute)
'''


from load import *
from sort import *


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


def build_message_tree(messages, fanout):
	# sort the messages
	messages = sort_messages_by_time(messages)

	# get all the message files and make sure they're sorted
	message_files = glob.glob('./messages/*.dat')
	message_files = sorted(message_files)

	# split the files and messages into fanout sized chunks
	file_names = chunks(message_files, fanout)
	message_chunks = chunks(messages, fanout)
	
	# get the first layer of the tree files
	layer = 0
	results = []
	for x in range(0, len(message_chunks)):
		results.append(write_message_node_initial(file_names[x], message_chunks[x], x, layer))

	# Loop until we create each layer down to the root
	layer = 1
	while len(results) > 1:
		result_chunks = chunks(results, fanout)
		results = []
		i = 0
		for chunk in result_chunks:
			files = []
			dates = []
			for file, date in chunk:
				files.append(file)
				dates.append(date)
			if len(result_chunks) < 2:
				# I AM GROOT!!!!!!!!!
				results.append(write_message_node(files, dates, i, "GROOOT"))
			else:
				results.append(write_message_node(files, dates, i, layer))
			i += 1
		layer += 1

	return results


def write_message_node_initial(files, messages, name, layer):
	dates = [m.date for m in messages]
	return write_message_node(files, dates, name, layer)


def write_message_node(files, dates, name, layer):
	# set up the struct to pack the data correctly
	# num | filename | hour, minute | filename | hour, minute |filename
	string = 'i64s'
	for x in range(0, len(files)-1):
		string += 'ii64s'
	s = struct.Struct(string)

	# open the file
	filename = './messages/tree/{0}_{1}.dat'.format(pad_zeroes(layer), pad_zeroes(name))
	f = open(filename, 'wb')

	# prepare the data to pack
	output = []
	for x in range(0, len(files)):
		output.append(files[x])
		if x != len(files)-1:
			output.append(dates[x].hour)
			output.append(dates[x].minute)
	data = [len(files)+len(dates)-1] + output
	# write the data
	f.write(s.pack(*data))
	f.close()
	return (filename, dates[len(dates)-1])

