"""
this is a program that checks the validity of the given post numbers
"""


#functions
def valid_post_number(post_number:str) -> str|bool:
    if len(post_number) != 11:
        return False
    if post_number[5] != "-":
        return False
    first_part = post_number[:5]
    second_part = post_number[6:]
    if not (first_part.isdigit() and second_part.isdigit()):
        return False
    return post_number
#main code
valid_postnumber = []
how_many_times = int(input("how many times do you want to use this program? "))
for i in range(how_many_times):
    check_post_number = input("enter the post number: ")
    postnumber = valid_post_number(check_post_number)
    if not postnumber == False:
        valid_postnumber.append(postnumber)
print(f'valid post numbers: {valid_postnumber}')

