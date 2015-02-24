class Time(object):

	def __init__(self, *args):
		self.hours = args[0]
		self.minutes = args[1]
		self.seconds = args[2]

	def convert_to_seconds(self):
		return self.hours * 60**2 + self.minutes * 60 + self.seconds

	def __lt__(self, other):
		return True if self.convert_to_seconds() < other.convert_to_seconds() else False

	def __gt__(self, other):
		return True if other.__lt__(self) else False

	def __eq__(self, other):
		return True if self.convert_to_seconds() == other.convert_to_seconds() else False

	def __ne__(self, other):
		return True if self.convert_to_seconds() != other.convert_to_seconds() else False
