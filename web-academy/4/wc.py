"""Word counter

Це програма з консольним інтерфейсом, яка може рахувати
рядки, символи, слова у файлі. Вона використовує
стандартний модуль `argparse` для того, щоб задати
інтерфейс.

Нею можна користуватися з терміналу так:

> python3 wc.py wc_test.txt -l -w -L
wc_test.txt
lines: 3
words: 7
max line length: 12

> python3 wc.py --help
usage: wc.py [-h] [-l] [-w] [-L] [file]

Count things in a file.

positional arguments:
  file                  input file

optional arguments:
  -h, --help            show this help message and exit
  -l, --lines           count lines
  -w, --words           count words
  -L, --max-line-length
                        max line length


де wc_test.txt адреса будь-якого текстового файлу

Завдання — доповнити 4 функції нижчe, щоб програма працювала.

Зауваження. file_handle – це уже відкритий файл, у функціях
можна зразу починати ітерувати по ньому.

"""


def count_lines(file_handle):
    """Return number of lines in file"""
    count = 0

    for line in file_handle:
        count += 1

    file_handle.seek(0)
    return count


def count_letters(file_handle):
    count = 0

    for line in file_handle:
        count += len(line)
    
    file_handle.seek(0)
    return count


def count_words(file_handle):
    count = 0

    for line in file_handle:
        wordsInLine = len(list(line.split(' ')))
        count += wordsInLine

    file_handle.seek(0)
    return count


def max_line_length(file_handle):
    result = 0
    lineLength = []

    for line in file_handle:
        lineLength.append(len(line))

    result = max(lineLength)

    file_handle.seek(0)
    return result


import sys
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Count things in a file.')

    parser.add_argument('file', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin, help='input file')
    parser.add_argument('-l', '--lines', action="store_true",
                        help='count lines')
    parser.add_argument('-t', '--letters', action="store_true",
                        help='count letters')
    parser.add_argument('-w', '--words', action="store_true",
                        help='count words')
    parser.add_argument('-L', '--max-line-length', action="store_true",
                        help='max line length')

    args = parser.parse_args()

    print(args.file.name)

    if args.lines:
        print('lines:', count_lines(args.file))

    if args.letters:
        print('letters:', count_letters(args.file))

    if args.words:
        print('words:', count_words(args.file))

    if args.max_line_length:
        print('max line length:', max_line_length(args.file))
