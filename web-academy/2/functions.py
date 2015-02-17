
# 1
def reverse(s):
    """
    Дзеркально обертає рядок
    """
    characters = list(s)
    charactersLengh = len(s)
    res = []
    i = 1
    while i <= charactersLengh:
        res.append(characters[i * -1])
        i += 1
    return ''.join(res)

assert reverse('abc') == 'cba'


# 2
def sum_of_squares_of_digits(n):
    """
    Рахує суму цифр числа
    """
    numbers = str(n)
    res = 0
    for number in numbers:
        res += int(number)
    return res


assert sum_of_squares_of_digits(256) == 13
assert sum_of_squares_of_digits(512) == 8
assert sum_of_squares_of_digits(111) == 3


# 3
s = [1, 2, 3]
def reverse_in_place(c):
    """
    Дзеркально повертає елементи списку, модифікуючи
    сам список
    """
    i = 1
    while i <= len(c):
        inverted = c.pop(i * -1)
        c.append(inverted)
        i += 1
    return c


reverse_in_place(s)
assert s == [3, 2, 1]


# *4
def generate_substrings(s):
    """
    Повертає множину послідовних підрядків рядка s
    """
    pass

# assert generate_substrings('abc') == \
    # set('a', 'b', 'c', 'ab', 'bc', 'ac', 'abc')

