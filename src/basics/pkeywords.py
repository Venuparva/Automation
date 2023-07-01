#!/usr/bin/python
from mod1 import print_pwd
import os as linuxadmin
# list of keywords in python
''' and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return
def       for       lambda    try '''
import keyword
print len(keyword.kwlist)
print keyword.kwlist
# Below function contains all keywords in it
result = "muthu kumar"
def all_keywords_python():
	global result
	result = "venu sakthi"
	i = ''
  	#i = 0  TypeError: 'in <string>' requires string as left operand, not int
  	if "venu" in result:
 		print "yes both are same"
	elif "Venu" in result:
		print "ignore case also same"
	else:
		print "nothing true"
	for i in result:
		print i
		if i == "n":
			pass
		elif i == "u":
			continue
		elif i == "s":
			break
	if len(result) == 2 and "venu" in result:
		print "im here-1"
	elif len(result) == 4 or "venu" in result:
		print "im here-2"	
	elif "sak" not in result:
		print "im here-3"
	#assert(len(result)*200 <= 100),"Colder than absolute zero!"
        # o/p of above line
	# AssertionError: Colder than absolute zero!
	#An assertion is a sanity-check that you can turn on or turn off when you are done with your testing of the program,Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.
 	cmd = '''print "exec command o/p: hello" '''
 	exec cmd # o/p "exec command o/p: hello"
        print eval('2'+'2') # argument must be string (or) code object,here o/p is 22
	#raise NameError('HiThere') # o/p is NameError: HiThere,The raise statement allows the programmer to force a specified exception to occur
	print "---------"
	try:
		if 1/0:
			pass
	except ZeroDivisionError as err:
		print " number of length of string not divided by zero"
		return None
	finally: # execute this finally block before above return statement executed
		print "execute this before except returns"
class Keywords():
	"""All keywords in this file"""
	h = all_keywords_python()
c = Keywords()
print c.h
del c
print linuxadmin.popen('date').read()
print "global variable modifed result",result
# you can change the value of result in the module-scope from within all_keywords_python() if you use the global keyword.

print print_pwd() # here notice the use of FROM keyword i.e its importing this print_pwd() function from another python file mod1.py which contains in it ,using from mod1.py import print_pwd() statment
#LAMBDA function,note that no need of return statment in lambda function here

def f (x): return x**2
print f(8)

g = lambda x: x**2
print g(8)
##############
#LAMBDA FUNCTION
##############
'''
>The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. 
>These functions are throw-away functions, i.e. they are just needed where they have been created. 
>Lambda functions are mainly used in combination with the functions filter(), map() and reduce().
>Guido van Rossums preferred List Comprehensions,but to make coding simpler,he designed all above functions
> General Syntax:
-----------
>lambda argument_list: expression
>lambda x,y : x+y
-----------
'''
##############
#FILTER/MAP/REDUCE functions
##############
#####
MAP
######
'''
map() is a function with two arguments:
-------------
r = map(func, seq)
-------------
>The first argument func is the name of a function and the second a sequence (e.g. a list) seq. 
>map() applies the function func to all the elements of the sequence seq. 
>It returns a new list with the elements changed by func
Example:
print map(lambda x: x+100,foo) # Apply some operation on all elements in list,i.e asdd by 100,o/p is [102, 103, 104, 105, 106]
'''
###########
FILTER
########
'''
> The filter(function, list) offers an elegant way to filter out all the elements of a list, 
for which the function returns True. 
>The function filter(f,l) needs a function f as its first argument and l as list second argument. 
f returns a Boolean value, i.e. either True or False. 
>This function will be applied to every element of the list l. 
>Only if f returns True will the element of the list be included in the result list.
---------
filter(function,list)
--------
Example:
print filter(lambda x: x%2 == 0,foo) # [2, 4, 6],getting only even numbers,functtion = "lambda x: x%2 == 0 " &  list = "foo"
---------
'''
###############
###REDUCE
###############

>The function reduce(func, seq) continually applies the function func() to the sequence seq. 
>It returns a single value. 


If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
>At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
>In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
>The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
>Continue like this until just one element is left and return this element as the result of reduce()
We illustrate this process in the following example:
------------
reduce(fun,seq)
------------
example:
print  reduce(lambda x,y: x+y, [47,11,42,13])
113
foo = [2,3,4,5,6]
print filter(lambda x: x%2 == 0,foo) # [2, 4, 6],getting only even numbers
print map(lambda x: x+100,foo) # Apply some operation on all elements in list,i.e asdd by 100,o/p is [102, 103, 104, 105, 106]
print reduce(lambda x, y:x+y,foo) # Reduce all elements to single one, o/p is 20

#WITH block,here to perform 2 related operations together,The classic example is opening a file, manipulating the file, then closing it:here it will close the file automatically

with open('output.txt', 'w') as f:
    f.write('Hi there!')
#f.write("venu") # throws error,bcz WITH statement already closed the file,hence error ::ValueError: I/O operation on closed file
r = 0
while r < 10:
	r = r + 1
	print r
print "***************"
print "ITERATORS & GENERATORS"
#ITERATORS : [] //same as list
#GENERATORS : () //execuete only onc time
#Iterators & Generators & yield
#Generators are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly:
#-----------
#general:
#-----------

list = [1,2,3]
for i in list:
	print i
print "-------"
#-----------
#Iterators:
#-----------
list = [x*x for x in range(3)]
for i in list:
	print i
print "-------"
#-----------
#Generators: same as iterator syntax but use () instead of [],also it will execute only once,not more than one time
#-----------
list = (x*x for x in range(3))
for i in list:
	print i
#calling second time # printing empty values
for i in list:
	print i
#BUT you can not perform for i in list a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.
'''
Example below
>>> list = (x*x for x in range(3))
>>> for i in list:
...     print i
...
0
1
4
>>> for i in list:
...     print i
...
>>>
'''
#-----------
#yield
#Yield is a keyword that is used like return, except the function will return a generator,instead of value
#-----------
print "yield o/p below"
def yfun():
	list = range(3)
	for i in list:
		yield i*5
print yfun() # <generator object yfun at 0x10c8a3370> # returning function() not value
res = yfun()
for i in res:
	print i

#complete o/p below:
31
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
yes both are same
v
e
n
u

s
im here-2
exec command o/p: hello
22
---------
 number of length of string not divided by zero
execute this before except returns
None
Sun Jun  5 00:06:08 PDT 2016

global variable modifed result venu sakthi
/Users/venu 1/Documents/python_tips

64
64
[2, 4, 6]
[102, 103, 104, 105, 106]
20
1
2
3
4
5
6
7
8
9
10
***************
ITERATORS & GENERATORS
1
2
3
-------
0
1
4
-------
0
1
4
yield o/p below
<generator object yfun at 0x10b360410>
0
5
10
###################
#Tricky interview Questions
###############

#********************
def Multi():
        return [lambda x : i*x for i in range(4)] // range(4) means [0,1,2,3]
print [m(2) for m in Multi()]

#here calling Multi() function with arg value is 2 therefore lambda 2 : 0*2 = "0" , 2: 1*2 = "2" , 4 : 2*2 = "4", 6 : 3*2 = "6" hence [0,2,4,6] will be human error o/p
################
Err o/p:
[0,2,4,6]
#-------------
Acutual o/p:
[6,6,6,6]
################

Due to LATE BINDING - during one time call itself,it will end with up with value of 3,since m(2) is passed,3*2 = 6 is printing all times means [3,3,3,3] * 2
The reason for this is that Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called.
------
More info:
when any of the functions returned by multipliers() are called, the value of i is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the for loop has completed and i is left with its final value of 3.
---------
In order to get expected o/p need to change the function like below
def Multi():
        return [lambda x,i=i: i*x for i in range(4)] // range(4) means [0,1,2,3]
print [m(2) for m in Multi()]
-----
Using Generator
def multi():
	for i in range(4): 
		yield lambda x : i*x
