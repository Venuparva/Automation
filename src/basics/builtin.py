import os

print "built-in functions"
#Built-in Functions		
bfun = '''
abs()	divmod()	input()	open()	staticmethod()
all()	enumerate()	int()	ord()	str()
any()	eval()	isinstance()	pow()	sum()
basestring()	execfile()	issubclass()	print()	super()
bin()	file()	iter()	property()	tuple()
bool()	filter()	len()	range()	type()
bytearray()	float()	list()	raw_input()	unichr()
callable()	format()	locals()	reduce()	unicode()
chr()	frozenset()	long()	reload()	vars()
classmethod()	getattr()	map()	repr()	xrange()
cmp()	globals()	max()	reversed()	zip()
compile()	hasattr()	memoryview()	round()	__import__()
complex()	hash()	min()	set()	
delattr()	help()	next()	setattr()	
dict()	hex()	object()	slice()	
dir()	id()	oct()	sorted() '''
print bfun
bfun = bfun.split()
print len(bfun)
#Total : 76 functions
#Non-Essential built in functions
#apply(), buffer(), coerce(), and intern().
print "#######################"
print "----------"
#abs:Return the absolute value of a number. The argument may be a plain or long integer or a floating point number. If the argument is a complex number, its magnitude is returned. 
print "----------"
print abs(0.3),abs(-45),abs(2+3j),abs(5353865348) # o/p is 0.3 45 3.60555127546 5353865348
print "----------"
#all(iterable) Return True if all elements of the iterable are true (or if the iterable is empty).
print "----------"
def all(iterable):
	for item in iterable:
		if not item:
			return False
		return True
print all([1,2,3,4]) # True
print all([]) # None
print all([1,'venu',3,4]) # True
print "----------"
#any(iterable) Return True if any of element of the iterable are true (or if the iterable is empty).
print "----------"
def any(iterable):
	for item in iterable:
		if item:
			return True
		return False
print any([1,2,3,4]) # True
print any([]) # None
print any([1,'venu',3,4]) # True
print "----------"
#basestring() : top to bottom order hierarchy reference
print "---------"
'''
Hierarchy:
            Object
              |
	  basestring
	   |       |
	string    unicode

>>> string1 = "I am a plain string"
>>> string2 = u"I am a unicode string"
>>> isinstance(string1, str)
True
>>> isinstance(string2, str) # both unicode & string in same level in hierarchy,hence its false
False
>>> isinstance(string1, unicode) # same like above case
False
>>> isinstance(string2, unicode)
True
>>> isinstance(string1, basestring) # String is child of basestring in hierarchy,hence its True
True
>>> isinstance(string2, basestring) # Unicode also child of basestring in hierarchy,hence its True
True			
'''
print "-----------"
#bin : to convert any integer to its binary value
#zfill : Return a copy of the string left filled with ASCII '0' digits to make a string of length width
print "-----------"
print bin(8)# 0b1000
print bin(8)[1:].zfill(8)# 000b1000
print bin(8)[2:].zfill(4)# b1000
print bin(8).zfill(4)# 0b1000
print bin(8)[2:].zfill(2)# 1000 ,here we need to fill 0b,mean first & second character to be filled with zfill hence [2:] is given
print "-----------"
#bool : return TRUE r FALSE
print "-----------"
a = 5
print bool(a > 4) # True
print bool(a < 3) # False	
print bool(0) # False
print bool(-1) # True
print bool([]) # False
print bool('') # False
print "---------------"
#Byte array()  Returns a mutable sequence of integers with values limited to the range 0 to 255 (inclusive)
print "---------------"
b = bytearray("hello world")
print b.find("w") # 6
#print b.append("test") # ValueError: string must be of size 1
b.append("?")
print b # hello worldw
print b.upper()
print b.startswith("H") # false,it should be True,if "h" given
b.extend("venu") # hello worldwvenu 
print b
print b[2] #  o/p is 108 Remember that the elements of a bytearray are integers, not strings
print chr(108) # o/p is "l"
b[0] = 'S' # conversion of char to ascii for us
print b # Sello worldwvenu
b[0] = 72 # You can provide an ascii integer if you want
print b
print b # Sello worldwvenu
print "---------------"
#callable Return True if the object argument appears callable, False if not. Note that classes are callable (calling a class returns a new instance);
print "---------------"
'''
>>> def sum(x,y):
...     return x+y
...
>>> callable(sum) # returning True since sum() function is callable
True
>>> x = 10
>>> callable(x)# varibale is not callable object
False
>>> class MyClass(object):
...     pass
...
>>> callable(MyClass)
True
>>> obj = MyClass()
>>> callable(obj) # Class object is not callable
False
'''
print "---------------"
print "chr"
#chr # Return a character whose ASCII code is the integer i. i must be in the range 0 to 255 (inclusive). chr() is the inverse of the function ord(),
print "---------------"
print chr(65) # A
print ord('A') # 65
print ord('B') # 66
print ord(chr(65)) # 65
#print chr(-1) # ValueError: chr() arg not in range(256),0 to 256
print "---------------"
#@classmethod: decorator for class method  & @staticmethod
print "---------------"
class MyClass(object):
	x = 15
	@classmethod
	def f1(cls):
		return 2 * cls.x
	@staticmethod
	def f2():
		return 2 * MyClass.x
print MyClass.f1() # 30
print MyClass.f2() # 30
class SubClass(MyClass):
	x = 20
print SubClass.f1() # 40 makes first parameter receive a reference to the class itself as opposed to the instance.,override happens due to classmthod
print SubClass.f2() # 30,same o/p since static method
print "---------------"
'''
cmp : comparison operator 
cmp(x,y) is not the same as cmp(y,x)
x < y : Negative ( -1)
x > y : Positive(1)
x == y : returns (0)
example:
>>> x = 1
>>> y = 2
>>> cmp(x,y)
-1
>>> cmp(y,x)
1
x = 2
>>> cmp(x,y)
0
'''
print "---------------"
'''
compile # compile the python code in 3 modes ,exec/single/eval
exec = complete execution of code
single = only check the first statemnt of code
eval = working only for expression in code,fails if its statement
Assume below code:
cat com.py
import os
x = 5
if (x > 3):
	print "yes"
else:
	print "no"
'''
with open('com.py') as f:
	content = f.read()
# EXEC mode:
code_obj = compile(content,'com.py','exec')
exec(code_obj) # o/p is "yes" coming from com.py and its working fine
# SINGLE mode:
code_obj = compile(content,'com.py','single')
exec(code_obj) #  since 'single' mode only generates bytecode for the first statement it encounters means import os,empty o/p
# EVAL mode:
#code_obj = compile(content,'com.py','eval') # SyntaxError: invalid syntax,throws error for import os,bcz its looking for exprssion
#exec(code_obj) # 
an_expression = "5+5"
code_obj = compile(an_expression,'<string>','eval') # working fine,since 5+5 is expression 
exec(code_obj) # 
#Note : The compile() function itself will raise a SyntaxError like normal syntax execution def fun(,if we leave liks this
print "---------------"
#Complex numbers: REAL & IMAGINARY part values
print "---------------"
x = complex(5,2) 
print x # (5+2j)
Z = (x.real, x.imag)
print x.real # 5.0
print x.imag # 2.0
y = complex(5,-2)
print y # (5-2j)
print x + y # (10+0j)
a = complex(4)
print a # (4+0j)
#From String ,create complex numbers
x = complex("4+2j")
print x  # (4+2j)
print complex() # 0j
print complex(0) # 0j
print "---------------"
# delattr to deletes the attribute with name attrname from the object.
class Myclass(object):
	x = 1
	def __init__(self):
		self.z = 3
objA = Myclass()
#delattr(objA,"x") # AttributeError: 'MyClass' object attribute 'x' is read-only
print objA.z # 3
#delattr(objA,"z") # AttributeError: 'Myclass' object has no attribute 'z',bcz its already deleted in previous line
#print objA.z
#delattr(objA,"y") # AttributeError: y,no such attribute exists
print "---------------"
#DICTIONARIES : ( from keyword Args/from another dictionaries/from iterables )
#dict(**kwargs), dict(dictionary, **kwargs), dict(iterable, **kwargs)
print "---------------"
print dict(a="1",b="2",emp="venu") # {'a': '1', 'b': '2', 'emp': 'venu'}
print dict(inner=dict(x="1",y="2"),z="3") # {'z': '3', 'inner': {'y': '2', 'x': '1'}}
mydict = { "name" : "venu","age":"30"}
print mydict # {'age': '30', 'name': 'venu'}
newdict = mydict
newdict['name'] = "sakthi"
print "after changing values got chnaged in both dictionairs"
print newdict # {'age': '30', 'name': 'sakthi'}
print mydict # {'age': '30', 'name': 'sakthi'}
print "after copying using dict() function not got chnaged in both dictionairs"
verynewdict = dict(mydict)
verynewdict['name'] = "muthu"
print verynewdict # {'age': '30', 'name': 'muthu'}
print mydict # still old value {'age': '30', 'name': 'sakthi'} not changed ,since used dict() function to copy
print "dictionaries from iterables"
print "----------"
#print dict(['x',10],['y',20]) #dict(list1 list2) # TypeError: dict expected at most 1 arguments, got 2
print dict([['x',10],['y',20]]) #dict( [ list1 list2 ] ) o/p is {'y': 20, 'x': 10} 
print dict([('x',10),('y',20)]) #dict( [ tuple1 tuple2 ] ) o/p is {'y': 20, 'x': 10}
#print dict (["abc.com","def.com"]) # ValueError: dictionary update sequence element #0 has length 7; 2 is required
print dict (["ab","de"]) # o/p is {'a': 'b', 'd': 'e'}
mylist = [('A',10),('B',30)]
print  dict(mylist) # {'A': 10, 'B': 30}
myset = set(mylist)
print myset # set([('A', 10), ('B', 30)])
print dict(myset) # {'A': 10, 'B': 30}
print "---------------"
# dir() function list out all avaible methods for particular method
mystr = "hello dsdds"
print dir(mystr)
"""o/p below
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] """
#print dict(mystr) # ValueError: dictionary update sequence element #0 has length 1; 2 is required
print "*****************"
print [x for x in dir("hello") if not x.startswith("_")]
print "---------------"
"""
dir() with no arguments It will return a list of all the variables in the current local scope
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> mystr = "Hello"
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'mystr']
>>> class MyClass(object):
...     pass
... 
>>> dir()
['MyClass', '__builtins__', '__doc__', '__name__', '__package__', 'mystr']
print "---------------"
"""
print "--------------"
a = 5
b = 2
q,r = divmod(a,b)
print "quotient,reminder",q,r # quotient,reminder 2 1,same will work with floating point numbers also
print "--------------"
#enumerate # enumerate() returns an iterator which yields a tuple that keeps count of the elements in the sequence passed
people = [ "venu","john","peter"]
print enumerate(people) # <enumerate object at 0x7f6ce8d25d20>
print list(enumerate(people)) # [(0, 'venu'), (1, 'john'), (2, 'peter')]
for i,p in enumerate(people):
	print i,p
"""o/p below
0 venu
1 john
2 peter
"""
#enumerate used to Performing operations over list elements
mylist = range(10)
print mylist # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i,element in enumerate(mylist):
	mylist[i] = element + 2
print mylist # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#eval(expr):
print eval('5+5')
x = 5
y = eval('x*5')
print y
def add(x):
	return x + 2
var = 5
print eval("add(%s)"%var) # 7
#Eval() function looks for variable in local scope,if not then look for global scope
x = 10
y = 15
def f():
	y=20
	return eval('x+y')
res = f()
print res # o/p is 30 y=20 and x = 10 ,taken x from outside n y from inside f()
#eval() allows you to override the globals() with your own dictionary.
x=4
y=2
myglobal = {"x":2,"y":3}
print eval('x+y',myglobal)#5
#Below case is bit reverse,Note that if you provide a globals dictionary, eval() will not look to the calling environment's globals if a variable does not exists in the provided globals dictionary.
y=4
myglobal = {"x":2}
#print eval('x+y', myglobal) # NameError: name 'y' is not defined
print eval('x+y', globals(),myglobal) # In order to fix above one,use globals() keyword and o/p is 6
#Object also getting evaluated using eval()
# globals() is useful for eval() -- if you want to evaluate some code that refers to variables in scope, those variables will either be in globals or locals.
code_obj = compile('5+5', '<string>', 'eval')
x = eval(code_obj)
print x # 10
#After EXEC ,only 1 example per keyword due to time constraint,refer below URL for more Examples
#http://joequery.me/code/python-builtin-functions/#classmethod
exec('print 5') # 5
print "**********"
# exec have 3 diff scenarios
#New functions can be defined, old functions can be overridden
myfn = '''
def fn(x): 
   return x+2  
     '''
#print fn(4) # NameError: name 'fn' is not defined
exec(myfn)
print fn(4) # 6
# An object, or one of its attributes, may be deleted
myfn = '''x=10 
x+5     '''
exec(myfn) # o/p is 15 
exec('del x')
#print x # NameError: name 'x' is not defined
#New Modules imported into scope
mystatements = '''
import math
def area_of_circle(radius):
   return math.pi * radius * radius '''
exec(mystatements)
print area_of_circle(5) # 78.5398163397
# unlike eval(),exec() has no return value
#y = exec('5+5') # inavlid syntax
exec('exec("print(10)")') # o/p is 10 exec inside exec
print "------------------"
# execfile() behaves similarly to exec(), but it executes statements located within a file instead of dealing with raw strings.
execfile('exec_file_fn_example.py')
#print is_perfectsquare(144) # function declared inside above file exec_file_fn_example.py
print "----------"
#file()  always prefer open() to open a file,use this "file" function in isinstance(file)
print "---------"
#filter() function Returns a list of the elements of iterable that returns a True value when passed to filter_function

mylist = [0,1,2,3,4,5,6,7,8,9]
def is_even(x):
     return x%2 == 0
print filter(is_even, mylist) # [0, 2, 4, 6, 8]
print "--------"
#float() # Convert a string or number x to floating point.but Attempting to convert a non-numeric value to float throws a ValueError:
x = 10 # integer
print float(x) # 10.0
x = "10" # string
print float(x) # 10.0
#print float("hello") # throws error
print "-----------"
#format() specification : to design html table & string formating < left > right ^ centre,so many other styles also there
#syntax : format(value, format_spec)
headers = ["First name", "last name"]
row1 = ["Joseph", "McCullough"]
row2 = ["Luke", "Wilczoch"]
row3 = ["MarKus", "Haley"]
tablerows = [headers, row1, row2, row3]
format_spec = "^15"
for first,last in tablerows:
	print (format(first,format_spec) + "|" + format(last,format_spec))
'''-----------
o/p below:
-----------
  First name   |   last name
    Joseph     |  McCullough
     Luke      |   Wilczoch
    MarKus     |     Haley '''
print "-----------"
'''
forzenset() -- are immutable,but set() are mutable
>>> mylist = [0,1,2,3]
>>> myset = set(mylist)
>>> # sets are mutable, we can add and remove elements
>>> myset.add(4)
>>> myset
set([0, 1, 2, 3, 4])
>>> myfrozenset = frozenset(mylist)
>>> # frozensets are immutable, you cannot add or remove elements
>>> myfrozenset.add(4) # it will throw error
'''
print "---------"
#getattr() : Returns the value of obj.attr. If the attr attribute does not exist and default was specified, default is returned. If default was not provided, AttributeError is raised.
var = "hello"
print getattr(var,"upper")() # HELLO
'''
>>> class MyClass(object):
...     x = 0
...     y = 1
...
>>> myobj = MyClass()
>>> getattr(myobj, "y")
1
>>> getattr(myobj, "someattr")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MyClass' object has no attribute 'someattr'
>>> getattr(myobj, "someattr", 20)
20
'''
print "--------"
#globals() # globals() is useful for eval() -- if you want to evaluate some code that refers to variables in scope, those variables will either be in globals or locals.
y=4
myglobal = {"x":2}
#print eval('x+y', myglobal) # NameError: name 'y' is not defined
print eval('x+y', globals(),myglobal) # In order to fix above one,use globals() keyword and o/p is 6
print "--------"
#hasattr() : useful to cehck whether the class object having particular attribute (or) not
#help : to invoke python in built help functions
#hex(x) : to convert interger to lowercase hexa decimal string prefixed with "0x"
'''
>>>
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
>>> hex(1L)
'0x1L'
'''
# id() : to print id() of the object at memory level
class Apple():
	def add():
		pass
objA = Apple()
print id(objA) # 4486503456
print "---------"
#input(): to get i/p from user
#user = input ( "enter the name:") # input() takes the raw_input() and performs an eval() on it as well.but raw_input gets input as normal string
#print user # NameError: name 'venu' is not defined
#user = raw_input("enter the name")
#print user # venu 
print "--------"
int() # for typecasting string/float to int objects
print "--------"
##You can use issubclass() or isinstance() functions to check a relationships of two classes and instances.
#The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.
#The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class
#in both cases is****( child,parent ) comes in order
print "--------"
#iter() #Return an iterator object.
'''
with open('mydata.txt') as fp:
    for line in iter(fp.readline, 'hello world'): # read lines from file till specific line contains "hello world" in it gets reached
        process_line(line)
'''
print "--------"
#len(s) : to returns the length of string (or) list etc
print "--------"
#list() : Mutable type 
print list("abc") # ['a', 'b', 'c']
print list("1234") # ['1', '2', '3', '4']
print "--------"
#locals # locals is read-only, globals is not,which will print local variables inside functions including arguments
print "--------"
def add(x):
	y=2
	print locals() # o/p is {'y': 2, 'x': 3} here its printing both local & global values
add(3)
print "--------"
#long() : Typecast int/float/str to long numbers
print "--------"
print long(2.5) # 2
#print long("3.5") # ValueError: invalid literal for long() with base 10: '3.5'
print long(23423422432423) # 23423422432423
print long("1003")# 1003
print "--------"
#The general syntax of a lambda function is quite simple:
################
#lambda argument_list: expression # lambda ARGLIST: EXPRESSION
#r = map(func, seq) Sytax for map # map(fun,seq) # it will apply the function operations() to all elements in seq
################
#FILTER/MAP/REDUCE functions
foo = [2,3,4,5,6]
print filter(lambda x: x%2 == 0,foo) # [2, 4, 6],getting only even numbers
print map(lambda x: x+100,foo) # Apply some operation on all elements in list,i.e asdd by 100,o/p is [102, 103, 104, 105, 106]
print reduce(lambda x, y:x+y,foo) # Reduce all elements to single one, o/p is 20
print "------"
print max(foo) # 6
print min(foo) # 2
print "------"
#memoryview() of function retruns memory view object created from given arg,
v = memoryview('abcefg')
print v[1] # b
print v[4] # f
print v[-1] # g
print v[1:4] # <memory at 0x77ab28>
print v[1:4].tobytes() # bce
#it has 2 methods
print v.tobytes() # abcefg
print v.tolist() # [97, 98, 99, 101, 102, 103]
print "---------"
#next() - retriesves next item from list by calling it in iterator
res = (x for x in foo if x == 3).next()
print res # o/p is 3
print "---------"
#object  class object base for all classes
print "---------"
#oct : converts any length integer to octal string,result is python valid expression
print oct(46827645389276584376587436) # 023274107371004010561676152254L 
print "---------"
#open() - fopen() to open files
print "---------"
#oct - represent unicode() of charcater
#print ord(a) # TypeError: ord() expected string of length 1, but int found
print ord('a') # 97 
print "---------"
#pow(x,y) - x to the power y
print pow(2,3) # 8
print "---------"
#print - To print the o/p,statemnts
print "---------"
#property : class future,needs to read more in future
print "---------"
#range - to create list
'''
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)
[0, 3, 6, 9]
>>> range(0, -10, -1)
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]
'''
print "---------"
#raw_input - to get raw input
print "---------"
#reload module - to reload thr previously imported module,have to read more
print "---------"
#repr - return string containing printable respresentatio  of object
x = "foo"
print repr(x) # 'foo'
print "---------"
#reversed - return the reversed iterator
list = range(5)
print list # [0, 1, 2, 3, 4]
print reversed(list) # <listreverseiterator object at 0x1043ba690>
for i in reversed(list):
	print i
'''
4
3
2
1
0'''
print "---------"
#round - to make rounoff
print round(3.1456) # 3.0
print round(3.1456,3) # 3.146
print round(1999)# 1999.0
#print round("2423") # TypeError: a float is required
print "---------"
#set - to convert list into set
print set(list) # set([0, 1, 2, 3, 4])
print "---------"
#slice - return sliced objected by indices
#a[start:stop:slice] or a[start:stop,i]
var = "hello world"
print var[1:4] # ell
print "---------"
print sorted(foo) # [2, 3, 4, 5, 6]
print "---------"
#@staticmethod,does not receive implicit first argument
print "---------"
#str() = For str typecasting
print str(4312421330) # '4312421330'
print sum(foo) # 20 ,add all values of foo
print "---------"
#SUper - returns proxy object that delegates method calls to parent (or) sibling class of type,only works for new style classes
'''
class C(B):
	def method(self,arg):
		super(C, self).method(arg)
'''
print "---------"
#tuple : immutable type,remains unchanged,use it for IP addr
print tuple("abcd") # ('a', 'b', 'c', 'd')
print "---------"
#type() - to find which type of object (or) datatype
print "---------"
#unichr - Returns unicode strung of one character
print unichr(97) # a
print "---------"
#unicode - Returns unicode version of string
var = "hello"
print unicode(var)
"""
## (ustring from above contains a unicode string)
> s = ustring.encode('utf-8')
> s
'A unicode \xc6\x8e string \xc3\xb1'  ## bytes of utf-8 encoding
> t = unicode(s, 'utf-8')             ## Convert bytes back to a unicode string
> t == ustring                      ## It's the same as the original, yay!
True"""
print "---------"
#vars - returns like __dict__ of the object
objA = MyClass()
print vars(objA)
print "---------"
print range(8) # [0, 1, 2, 3, 4, 5, 6, 7]
print xrange(8) # 
"""
>>> for i in xrange(1, 10, 2):
...     print(i)
...
1
3
5
7
9
"""
print "---------"
#zip - returns list of tuples
x = [1,2,3]
y = [4,5,6]
print zip(x,y) # [(1, 4), (2, 5), (3, 6)]
print "---------"



