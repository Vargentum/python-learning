class Human():
	"""docstring for Human"""
	def __init__(self, name):
		self.name = name

	def say_hello(self):
		print("Hi, I'm {}".format(self.name))
		

# Inherinance
class Student(Human):
	pass
		


paul = Human('Paul')
print(paul.name)
print(paul.say_hello())


mary = Student('Mary')
print(mary.name)
print(mary.say_hello())