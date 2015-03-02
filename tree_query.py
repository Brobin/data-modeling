

# start at the root
# go down the tree and find the sub-trees that would
# contain Nebraska
# work all the way down to the user files and return
# the count of users
def tree_nebraskans(filename):
	result = 0

	if "tree" in filename:

		root = open(filename, 'rb')
		number = struct.unpack('i', root.read(4))[0]

		content = []
		for x in range(0, number):
			content.append(struct.unpack('64s', root.read(64))[0].split('\x00', 1)[0])

		i = 1
		search = []
		found = False
		state = content[i]

		# while we haven't found Nebraska, skip to the next state
		while (i < len(content)-2) or (state == "Nebraska"):
			if (state > "Nebraska" and not found) or (state == "Nebraska" and found):
				# if we find Nebraska, add teh preceding file to the search list
				before = content[i-1]
				if before not in search:
					search.append(before)
				if not found:
					found = True
			# if the state is Nebraska, add it to the result
			if state == 'Nebraska':
				result += 1
			i = i + 2
			state = content[i]

		# recursively search each file for Nebraskans
		for file in search:
			result += tree_nebraskans(file)

	return result