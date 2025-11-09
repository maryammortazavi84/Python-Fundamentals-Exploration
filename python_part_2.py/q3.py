n = 5
def cal(n):
    if n==1:
        return 1
    result = cal(n-1) + (1/n)
    return(result)


print(cal(n))


