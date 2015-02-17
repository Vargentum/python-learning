
# 1
def reverse(s):
    """
    Дзеркально обертає рядок
    """
    pass

assert reverse('abc') == 'cba'

# 2
def sum_of_squares_of_digits(n):
    """
    Рахує суму цифр числа
    """
    pass

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
    pass

reverse_in_place(s)
assert s == [3, 2, 1]

# *4
def generate_substrings(s):
    """
    Повертає множину послідовних підрядків рядка s
    """
    pass

assert generate_substrings('abc') == \
    set('a', 'b', 'c', 'ab', 'bc', 'ac', 'abc')
