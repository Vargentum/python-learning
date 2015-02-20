fizz = 0
buzz = 0
fizzbuzz = 0

for item in range(100):

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

print('There are ' +str(fizz)+ ' Fizz.')
print('There are ' +str(buzz)+ ' Buzz.')
print('There are ' +str(fizzbuzz)+ ' FizzBuzz.')
