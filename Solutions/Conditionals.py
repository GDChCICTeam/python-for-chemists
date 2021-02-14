#!/usr/bin/env python3

# --------------------------------------------------------------------------- #
# Write if/else conditionals that decide what is printed to the console. The
# output should be based on the content of the strings in the given list. Test
# the following criteria and print the tested string along with the criteria
# that match. If several rules match, print all of them. Try to use built-in
# python functions wherever possible.
#
# Rules:
#   - contains only alphanumerical characters
#   - contains only alphabetical characters
#   - contains only digits (i.e. is a number)
#   - contains at least one special character
#   - none of the above
# --------------------------------------------------------------------------- #

list_of_strings = ['def', '213', '10deers', 'df$df#$ad']

for string in list_of_strings:
    if string.isalnum():
        print(string, '\n> Contains only alphanumerical characters')
        if string.isalpha():
            print('>> Contains only alphabetical characters\n')
        elif string.isdigit():
            print('>> Is a number\n')
        else:
            print('>> Contains numbers and alphabetical characters\n')
    else:
        print(string, '\n> Has at least one special character\n')
