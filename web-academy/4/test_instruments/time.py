class Time(object):

	secondsInMinute = 60
	secondsInHour = secondsInMinute**2

	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def convert_to_seconds(self):
		return (self.hours * Time.secondsInHour) + (self.minutes * Time.secondsInMinute) + self.seconds

	def __lt__(self, other):
		return True if self.convert_to_seconds() < other.convert_to_seconds() else False

	def __add__(self, other):
		totalSeconds = self.convert_to_seconds() + other.convert_to_seconds()
		print(totalSeconds)
		
		def prettify(n):
			result = []
			result.append(n // Time.secondsInHour)
			result.append(n % Time.secondsInHour // Time.secondsInMinute)
			result.append(n % Time.secondsInHour % Time.secondsInMinute)
			return Time(*result)

		return prettify(totalSeconds)


	def __gt__(self, other):
		return True if other.__lt__(self) else False

	def __eq__(self, other):
		return True if self.convert_to_seconds() == other.convert_to_seconds() else False

	def __ne__(self, other):
		return True if self.convert_to_seconds() != other.convert_to_seconds() else False
