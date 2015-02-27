
import datetime


class User():
	def __init__(self, id, name, location, messages = []):
		self.id = id
		self.name = name
		self.location = location
		self.messages = messages
	def __str__(self):
		return self.csv()
	def csv(self):
		return "{0};{1};{2}".format(self.id, self.name, self.location)

class Message():
	def __init__(self, id, user_id, date, text):
		self.id = id
		self.date = date
		self.text = text
		self.user_id = user_id
	def __str__(self):
		return self.csv()
	def csv(self):
		return "{0};{1};{2};{3}".format(self.id, self.user_id, self.date, self.text)
