"""
This program checks whether the first and last characters of a string
are the same. It also handles empty strings by asking the user to type something.
"""

def check_string(string):
    if len(string) == 0:
        return None
    elif string[0] == string[-1]:
        return True
    else:
        return False



string = input("enter string: ")
result = check_string(string)
if result:
    print("the first and last char are the same:)")
elif result == None:
    print("type something")
else:
    print("the first and last char are not the sam:(") 