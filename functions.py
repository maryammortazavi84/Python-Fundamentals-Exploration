"""
This program counts the number of uppercase and lowercase letters 
in a given string entered by the user.
"""


def count_letter (string):
    # initialize counters for uppercase and lowercase
    upper_counter = 0
    lower_counter = 0
    for char in string:
        if 64<ord(char)<91:
            # check if character is uppercase (A-Z)
            upper_counter += 1
        elif 96<ord(char)<123:
             # check if character is lowercase (a-z)
            lower_counter += 1
    return(upper_counter , lower_counter)
input_string = input("enter your string: ")
counting = count_letter(input_string)
upper_count , lower_count = counting
print(f'upper case :{upper_count} , lower case :{lower_count}')
    
