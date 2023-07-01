from itertools import permutations
s = "hello"
permsList = [str(''.join(x)) for x in permutations(s)]
print(permsList)

x = [[2,3],[1,2],[3,2],[5,4]]

print(sorted(x, key = lambda y: y[0]))
#def getSecondkey():
#    return x[1]
#res = sorted(key=getSecondkey())
#print("res",res)

temp = ['a','b','c','d','e','f','g']



