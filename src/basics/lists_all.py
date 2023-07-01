mylist = [1,2,3,4,5]
print mylist
print mylist[0]
print mylist[-1]
print mylist[:]
print mylist[-1:]
print mylist[:-1]
print "value-0",mylist[0:-1]
print mylist[-1:0]
print mylist[-3:]
print mylist + ["abdcc",5]
print "---------"
mylist[3] = 99
print mylist
mylist.append(55)
print mylist
mylist.append(5**6)
print "value-2",mylist
mylist[2:4]=['y','u','i']
print mylist
mylist[2:4]=[]
print "---------"
print mylist
mylist[:]=[]
print "value-3",mylist
print len(mylist)
list2 = ['r',3,5,'x']
newlist = [2,3,4]
x = [mylist,list2]
print "---------"
print x
print "value-4",x[0]
#print x[0][1] # IndexError: list index out of range
y = [newlist,list2]
print y[0][1]
##################
#Output below
################
"""
[1, 2, 3, 4, 5]
1
5
[1, 2, 3, 4, 5]
[5]
[1, 2, 3, 4]
value-0 [1, 2, 3, 4]
[]
[3, 4, 5]
[1, 2, 3, 4, 5, 'abdcc', 5]
---------
[1, 2, 3, 99, 5]
[1, 2, 3, 99, 5, 55]
value-2 [1, 2, 3, 99, 5, 55, 15625]
[1, 2, 'y', 'u', 'i', 5, 55, 15625]
---------
[1, 2, 'i', 5, 55, 15625]
value-3 []
0
---------
[[], ['r', 3, 5, 'x']]
value-4 []
3
###########
print "fibonacci series"
"""
a,b=0,1
while b<10:
	print b
	a,b=b,a+b
-------o/p below
1
1
2
3
5
8
------
i = 5*5
print i # 25
