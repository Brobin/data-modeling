
'''
Models to contain the data for Users and Messages
'''


from constants import USER_STRUCT, MESSAGE_STRUCT


class User():
	def __init__(self, id, first, last, city, state, messages = []):
		self.id = id
		self.first = first
		self.last = last
		self.city = city
		self.state = state
		self.messages = messages
	def __str__(self):
		return "{0};{1},{2};{3},{4}".format(self.id, 
			self.last, self.first, self.city, self.state)
	def byte(self):
		return USER_STRUCT.pack(self.id, 
			self.first, self.last, self.city, self.state)

class Message():
	def __init__(self, id, user_id, date, text):
		self.id = id
		self.date = date
		self.text = text
		self.user_id = user_id
	def __str__(self):
		return "{0};{1}".format(self.id, self.date)
	def byte(self):
		year = self.date.year
		month = self.date.month
		day = self.date.day
		hour = self.date.hour
		minute = self.date.minute
		return MESSAGE_STRUCT.pack(self.id, self.user_id, 
			year, month, day, hour, minute, self.text)

