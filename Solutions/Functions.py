#!/usr/bin/python3

# --------------------------------------------------------------------------- #
# Write three functions where each function has only one task. The tasks for
# the functions are:
#   - check if container is of type list
#   - check if list is empty
#   - print each element of list
# The printing function should only be called in the case that the two other
# functions have tested the container for type list and that its not emtpy
# --------------------------------------------------------------------------- #

a_list = ['element 1', 'element 2', 'element 3', 1, 2, 3,
          ['sublist element1', 'sublist element 2']]


# define function that tests container type
def container_is_list(container):
    return type(container) is list


# define function that tests if list is empty
def list_is_empty(list):
    return len(list) == 0


# define function that prints each element of a list
def print_each_element_of_list(_list):
    for element in _list:
        print(element)


# call the functions that were defined above
if container_is_list(a_list) and not list_is_empty(a_list):
    print_each_element_of_list(a_list)
