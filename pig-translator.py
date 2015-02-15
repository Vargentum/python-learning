"""
Pig translator change origin word, to word in which first letter becomes
a last one with the `ay` ending.
eg python translated to ythonpay
"""

print("Welcome to Pig translator.")
user_word = input("Type a word please: ")

def translate(str):
  modify_head = lambda x: x + 'ay'
  result = str[1:] + modify_head(str[0])
  return result

assert translate('abc') == 'bcaay'

print("Pig translator says:", translate(user_word))