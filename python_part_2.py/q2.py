v = int(input("please enter v (m/s): "))
t = int(input("please enter t (c): "))
def valid_input(v,t):
    if v<0 or t>10 :
        print("please enter a valid number!")
        return False
    else:
        return True
    

def calculation(v,t):
    top = 10*(v**0.5) - (10*v) + 10.5
    w = 33-((top * (33-t))/22)
    return(w)
    
validation = valid_input(v,t)
if validation:
    w = calculation(v,t)
    print(f'Wind Chill Index = {w}')

