
'''
Models to contain the data for Users and Messages
'''


import datetime
import struct


class User():
	def __init__(self, id, name, city, state, messages = []):
		self.id = id
		self.name = name
		self.city = city
		self.state = state
		self.messages = messages
	def __str__(self):
		return "{0};{1};{2},{3}".format(self.id, 
			self.name, self.city, self.state)
	def byte(self):
		return struct.pack('i64s32s32s', self.id, 
			self.name, self.city, self.state)

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
		return struct.pack('iiiiiii1024s', self.id, self.user_id, 
			year, month, day, hour, minute, self.text)

