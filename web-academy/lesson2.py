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





# Get all subsecquences from sequense ordered in alphabetical order:
def getSubSequences(str):
  sortedList = sorted(list(str))
  i = len(sortedList)

  case = ''

  for a in sortedList:
    for b in sortedList: 
      if a != b
        case += a + b


  return case

['a','b','c']



# assert getSubSequences('abc') == ['a','b','c','ab','bc','ac']
print(getSubSequences('abc'))