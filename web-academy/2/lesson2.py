# from pdb import pdb
err_msg = 'Invalid number. Try again.'

# Function that get sum of digits number passed to string
def getSumOfDigits(num):
  result = 0
  for digit in str(num):
    try:
      result += int(digit)
    except ValueError:
      result = err_msg
      break
  return result


assert getSumOfDigits(956) == 20
assert getSumOfDigits('ax1') == err_msg



# Define odd or even detection for value
def evenOrOdd(num):
  is_even = lambda n: n % 2 == 0

  try:
    return "Even" if is_even(num) else 'Odd'
  except TypeError:
    return err_msg

assert evenOrOdd(5) == 'Odd'
assert evenOrOdd(4) == 'Even'
assert evenOrOdd('ax1') == err_msg
