plain_text = "this is a simple text z"
cipher =""
for char in plain_text:
    if char != " ":
        index = ord(char)
        new_char = chr(index) 
    else:
        new_char = char
    cipher = cipher + new_char
print(cipher)
    
    
   