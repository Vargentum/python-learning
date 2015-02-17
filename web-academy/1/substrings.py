"""
Find substring from string and sort is in alphabetical order
"""

# sorting
def is_alphabetical(s):
	last_character = s[0]
	for character in s[1:]:
		if character < last_character:
			return False
		last_character = character
	return True

assert is_alphabetical('abcd')
assert not is_alphabetical('abdc')


# make
def generate_all_substrings(s):
	if s == '':
		return []
	elif len(s) == 1:
		return [s]
	else:
		tail = s[-1]  # last item
		head = s[:-1] # all except last

	head_substrings = generate_all_substrings(head)
	result = []
	import ipdb
	ipdb.set_trace()	
	for substring in head_substrings:
		result.append(substring + tail)
		result.append(substring)
	return result

print(set(generate_all_substrings('abc')))


'''
Find info about list, set, tuple, tuple
tuple is immutable

Find about `assert` keyword


		mutable		order	repeat		check		deletion	addition	reading	
list				yes		slow		slow		slow		fast		fast
dict				not		fast		fast		fast-slow	fast-slow	fast
set 	yes			not		not			fast		fast-slow	fast-slow	not
tuple	not			yes		yes			slow		not			not			fast




from collections import ordered dice



'''

