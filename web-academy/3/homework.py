import string
import collections
dataCounted = {}

def filter_bad_characters_1(data):
  result = [x for x in data if x in string.ascii_letters]
  return ''.join(result)



def filter_bad_characters_2(data):
    result = filter(lambda x: x in string.ascii_letters, data)
    return ''.join(list(result))

assert filter_bad_characters_1('%#%@# W @ O #@# RD 2,,,') == 'WORD'
assert filter_bad_characters_2('%#%@# W @ O #@# RD 2,,,') == 'WORD'


def char_distribution(data):
  result = {}
  global dataCounted
  dataCounted = collections.Counter(data)
  for i in dataCounted:
    result[i] = dataCounted[i]
  return result

assert char_distribution('aabbbcccc') == {'a': 2, 'b': 3, 'c': 4}



def most_common_char(data):
  for tpl in dataCounted.most_common(1):
    for key in tpl:
      return key

assert most_common_char('aabbbcccc') == 'c'


def least_common_char(data):
  result = ''
  for key, value in dataCounted.items():
    if dataCounted.min() == value:
      return key

print(least_common_char('aabbbcccc'))

