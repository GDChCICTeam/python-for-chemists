#!/usr/bin/python3

# --------------------------------------------------------------------------- #
# write if/else conditionals that decide what is printed to the console
# based on the content of the strings that are stored in the given list
# the following criteria should be tested and tested string should be printed
# together with a messages indicating which of the following rules matched. In
# case that several rules apply, several messages shall be printed.
# Rules:
#   - contains only alphanumerical characters
#   - contains only alphabetical characters
#   - contains only digits
#   - contains at least one special character
#   - none of the above
# --------------------------------------------------------------------------- #

list_of_strings = ['def', '213', '10deers', 'df$df#$ad']

for string in list_of_strings:
    if string.isalnum():
        print(string, '\n> Has alphanumerical characters')
        if string.isalpha():
            print('>> Has only alphabetical characters\n')
        elif string.isdigit():
            print('>> Is a digit\n')
        else:
            print('>> Has numbers and alphabetical characters\n')
    else:
        print(string, '\n> Has at least one special character\n')
