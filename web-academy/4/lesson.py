""" Word counter """


def count_lines(file_path):
	count = 0
	with open(file_path) as file_handle:
		for line in file_handle:
			count += 1
	return count


def count_words(file_path):
	count = 0
	with open(file_path) as file_handle:
		for line in file_handle:
			wordsInLine = line.split()
			count += len(wordsInLine)
	return count
			


def count_symbols(file_path):
	count = 0
	with open(file_path) as file_handle:
		for line in file_handle:
			count += len(line.strip())
			# count += len(line[:-1] if line[-1] == '\n' else line)
	return count


def max_line_length(file_path):
	with open(file_path) as file_handle:
		# Generator expression ()
		# List comprehension []
		allLength = (len(x) for x in file_handle)
		return max(allLength)



if __name__ == '__main__':
	file_path = 'test.txt'
	print(count_lines(file_path))
	print(count_words(file_path))
	print(count_symbols(file_path))
	print(max_line_length(file_path))
