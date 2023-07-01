def fibo(n):
    ''' 0 1 1 2 3 5 8 13'''
    if n < 0:
        print("invalid i/p")
    elif n == 0:
        return 0
    elif n == 1 or n ==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print("-------")
print(fibo(3))
print(fibo(2))
print("-------")
res = fibo(4)
print(res)# => 1+1+2+3 = 7

