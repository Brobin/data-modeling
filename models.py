
import datetime
import struct


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
	def byte(self):
		return struct.pack('i64s64s', self.id, self.name, self.location)

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
	def byte(self):
		year = self.date.year
		month = self.date.month
		day = self.date.day
		hour = self.date.hour
		minute = self.date.minute
		return struct.pack('iiiiiii1024s', self.id, self.user_id, 
			year, month, day, hour, minute, self.text)

