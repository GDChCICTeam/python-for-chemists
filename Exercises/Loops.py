#!/usr/bin/env python3
import errno
import pathlib
import sys

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
