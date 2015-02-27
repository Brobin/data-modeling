
import datetime
import glob

from models import User, Message


def load_users():
	users = []
	messages = load_messages()

	for user_file in glob.glob('./csv/users/*.csv'):
		user_file = open(user_file)
		data = user_file.readline()
		data = data.split(";")
		user = User(int(data[0]), data[1], data[2])
		users.append(user)
		print(str(user))

	return users


def load_messages():
	messages = []
	for message_file in glob.glob('./csv/messages/*.csv'):
		message_file = open(message_file)
		data = message_file.readline()
		data = data.split(";")
		date = date_parse(data[2])
		message = Message(int(data[0]), int(data[1]), date, data[3])
		messages.append(message)
		
	return messages


def date_parse(s):
    try:
        return datetime.datetime(int(s[0:4]),int(s[5:7]),int(s[8:10]), int(s[11:13]), int(s[14:16]), int(s[17:19]))
    except:
    	return None


users = load_users()
