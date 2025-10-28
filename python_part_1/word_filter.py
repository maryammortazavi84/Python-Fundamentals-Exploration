filter_text = ['test1', 'test2']
string = 'test1 test2 test3 test4 test5'
string = string.split()  
for i, word in enumerate(string):  
    if word in filter_text:
        string[i] = '*****' 
result = ' '.join(string)  
print(result)




