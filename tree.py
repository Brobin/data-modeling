
'''
Builds B+ trees for the tables
'''


from load import load_users, load_messages


# Root node contains n pointers to more files
# those files either contain data or pointers
# the next level of files.
def build_user_tree(users, n):
	length = len(users)
	depth = 0
	while length / (n ** depth) > 0:
		depth = depth + 1
	return depth

users = load_users()
num = build_user_tree(users, 10)
print(num)
print(len(users) - 10**(num-1))


