class Car():
	def __init__(self, color):
		self.color = color
		
	def go(self):
		print("Going")

	type = 'oil'

	def get_type(self):
		print("This is %s type" % self.type)


class ElectroCar():
	type = 'electric'


class Ferrari(Car):
	def __init__(self):
		self.color = "Red"
	

class Tesla(ElectroCar, Car):
	pass
		

car = Car('Blue')
car.go()
print(car.color)
		
ferrari = Ferrari()
ferrari.go()
print(ferrari.color)

myCar = Tesla('Black')
print(myCar.type)
myCar.go()
