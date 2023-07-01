import os
#Factorial
print "-------"
#6! = 1*2*3*4*5 = 120
input = raw_input("enter the i/p")
print input
b = i = 1
while i < int(input):
	i=i+1
	b=i*b
	print b
 	if i == input:
		break
#finbonacci series
print "-------"
a,b=0,1
while i < int(10):
	print b
	i = i + 1
	a,b=b,a+b
#sqaure of number
print "-------"
res = int(input)**2
print res
