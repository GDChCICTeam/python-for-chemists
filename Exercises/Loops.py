#!/usr/bin/python3
import pathlib
import errno

root_dir = pathlib.Path.cwd().parent
data_path = root_dir / 'Data'
data_file = root_dir / 'Data' / 'input_for_loop_exercise.txt'

# --------------------------------------------------------------------------- #
# traverse the content of the variables 'content', 'a_dictionary', 'a_list' with:
#   - while loop
#   - for loop
# and print each element using the print() function
# --------------------------------------------------------------------------- #


# parse content of file 'input_for_loop_exercise.txt'
content = ''
if data_file.exists():
    with data_file.open() as infile:
        content = infile.read().split('\n')
else:
    exit(errno.ENOENT)

# --------------------------------------------------------------------------- #

# initialize dictionary and list
a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a_list = ['a', 'b', 'c', 'd']
