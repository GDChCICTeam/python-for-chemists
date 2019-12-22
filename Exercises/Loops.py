#!/usr/bin/python3

# --------------------------------------------------------------------------- #
# traverse the content of the variables 'content', 'a_dictionary', 'a_list' with:
#   - while loop
#   - for loop
# and print each element using the print() function
# --------------------------------------------------------------------------- #

# this is only to parse data from the file with test data and store it in the
# variable content
with open('../Data/input_for_loop_exercise.txt') as input_file:
    content = [i.strip('\n') for i in input_file.readlines()]
# initialize dictionary and list
a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a_list = ['a', 'b', 'c', 'd']
