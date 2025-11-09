string = input("please enter your string: ")
replacment = ['a' , 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
new_string = ""
string = string.replace(" " , "")
for char in replacment:
    string = string.replace(char , '*')
for chars in string:
    if chars.islower():
        new_string = new_string + chars.upper()
    elif chars.isupper():
        new_string = new_string + chars.lower()
    else:
        new_string = new_string + chars
        
print(new_string)

    