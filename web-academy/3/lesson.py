

def has_no_e(word):
	return 'e' in word

assert has_no_e('eat')
assert not has_no_e('has')



def is_letter_in_word(word, letter):
	return letter in word

assert is_letter_in_word('eat','a')
assert not is_letter_in_word('eat','b')



def avoids(word, forbidden):
	for letter in word:
		if letter in forbidden:
			return False
	return True

assert avoids('hello', 'ab')
assert not avoids('hello', 'al')


def uses_only(word, allowed):
	for letter in word:
		if letter not in allowed:
			return False
	return True

assert uses_only('hello', 'olehen')
assert not uses_only('hello', 'hela')



def uses_all(word, allowed):
	for letter in word:
		if letter not in allowed:
			return False
	if len(word) != len(allowed):
		return False
	else:
		return True

assert uses_all('word', 'wdro')
assert not uses_all('word', 'wodoro')
assert not uses_all('word', 'wdroa')


def is_palindrome(word):
	i = 1
	while i <= len(word) // 2:
		if word[i-1] != word[-i]:
			return False
		i += 1
	return True
	
assert is_palindrome('abccba')
assert is_palindrome('abcba')
assert not is_palindrome('abccbc')
