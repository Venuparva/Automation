from functools import reduce


def lambdafuns(inputDict: dict)-> int:
    evenCount = reduce(lambda x,y:( y+(filter(lambda z: z%2==0,inputDict))),inputDict)
    print("evenCount:%s"% evenCount)

lambdafuns(inputDict = {'a':1,'b':2, 'c':3,'d':4})
