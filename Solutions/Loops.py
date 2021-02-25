#!/usr/bin/env python3
import errno
import pathlib
import sys

if pathlib.Path.cwd().name == 'python-for-chemists':
  root_dir = pathlib.Path.cwd()
else:
  root_dir = pathlib.Path.cwd().parent

data_path = root_dir / 'Data'
data_file = root_dir / 'Data' / 'input_for_loop_exercise.txt'

# --------------------------------------------------------------------------- #
# Traverse the content of the variables 'content', 'a_dictionary', 'a_list'
# with:
#
#   - a while loop
#   - a for loop
#
# and print each element using the print() function. Afterwards, take a look at
# the file 'input_for_loop_exercise.txt' in the 'Data' folder. Try to make
# sense of the code below. What does it do?
# --------------------------------------------------------------------------- #


# parse content of file 'input_for_loop_exercise.txt'
CONTENT = ''

if data_file.exists():
    with data_file.open() as infile:
        CONTENT = infile.read().split('\n')
else:
    sys.exit(errno.ENOENT)

# --------------------------------------------------------------------------- #

# initialize dictionary and list
a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a_list = ['a', 'b', 'c', 'd']

print('Printing all elements of content with while loop:')
counter = 0
while counter < len(CONTENT):
    print(CONTENT[counter])
    counter += 1


print('Printing all elements of content with for loop:')
for line in CONTENT:
    print(line)


print('Printing all elements of list with while loop:')
counter = 0
while counter < len(a_list):
    print(counter, ': ', a_list[counter])
    counter += 1


print('Printing all elements of list with for loop:')
counter = 0
for element in a_list:
    print(counter, ': ', element)
    counter += 1


print('Printing all elements of dict with while loop:')
keys = list(a_dictionary.keys())
counter = 0
while counter < len(keys):
    print(keys[counter], ': ',  a_dictionary[keys[counter]])
    counter += 1


print('Printing all elements of dict with for loop:')
counter = 0
for key in a_dictionary.keys():
    print(counter, ': ', a_dictionary[key])
    counter += 1
