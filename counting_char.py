"""
counting the chars in a string
"""
counting_chars = {}
input_string = input("enter your string: ")
input_string = input_string.replace(" " , "")
for char in input_string:
    if char in counting_chars:
        counting_chars[char] +=1
    else:
        counting_chars[char] = 1
print(counting_chars)
