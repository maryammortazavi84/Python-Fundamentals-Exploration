filter_text = ['test1' , 'test2']
string = 'test1 test2 test3 test4 test5'
string = string.split()
for word in string:
        if word in filter_text:
            word = '*****'
print(string)



