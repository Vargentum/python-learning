def fizzbuzz(start, end):
	fizz = 0
	buzz = 0
	fizzbuzz = 0

	for item in range(start,end):

		if item % 3 == 0 and item % 5 == 0:
			print('FizzBuzz ' + str(item))
			fizzbuzz += 1

		elif item % 3 == 0:
			print('Fizz ' + str(item))
			fizz += 1

		elif item % 5 == 0:
			print('Buzz ' + str(item))
			buzz += 1

		else:
			print(item)
