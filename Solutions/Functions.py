#!/usr/bin/env python3

# --------------------------------------------------------------------------- #
# Write three functions that each has exactly one task. The tasks for the
# functions are:
#
#   - check if a given container is of type list
#   - check if a given list is empty
#   - print each element of a given list
#
# Afterwards, analyze the variable named a_list given below. Use the printing
# function once you confirmed that a given container is of type list and is not
# emtpy.
# --------------------------------------------------------------------------- #

a_list = ['element 1', 'element 2', 'element 3', 1, 2, 3,
          ['sublist element1', 'sublist element 2']]


def container_is_list(container):
    """This function tests whether a given container is of type list"""
    return isinstance(container, list)


# function that tests if list is empty
def list_is_empty(_list):
    """This function tests whether a given list is empty"""
    return len(_list) == 0


def print_each_element_of_list(_list):
    """This function prints all elements of a list"""
    for element in _list:
        print(element)


# call the functions that were defined above and analyze a_list
if container_is_list(a_list) and not list_is_empty(a_list):
    print_each_element_of_list(a_list)
