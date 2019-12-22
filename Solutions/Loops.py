#!/usr/bin/python3

import os
import pathlib
import errno

# --------------------------------------------------------------------------- #
# traverse the content of the variables 'content', 'a_dictionary', 'a_list' with:
#   - while loop
#   - for loop
# and print each element using the print() function
# --------------------------------------------------------------------------- #

# this is only to parse data from the file with test data and store it in the
# variable content. It's written to work on the three major OSs.
script_dir = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
repo_home = pathlib.Path()
repo_home_list = [i for i in script_dir.parents if i.stem == 'github-cic-python-workshop']
if len(repo_home_list) == 0:
    print("Could not determine repository's home directory")
    exit(errno.ENOENT)
else:
    repo_home = repo_home_list[0]

data_file = repo_home.joinpath('Data/input_for_loop_exercise.txt')
content = ''
if data_file.exists():
    with data_file.open() as infile:
        content = infile.read().split('\n')
else:
    exit(errno.ENOENT)


# initialize dictionary and list
a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a_list = ['a', 'b', 'c', 'd']


print('Printing all elements of content with while loop:')
counter = 0
while counter < len(content):
    print(content[counter])
    counter += 1


print('Printing all elements of content with for loop:')
for line in content:
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
