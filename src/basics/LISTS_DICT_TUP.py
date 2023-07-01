################
# Python Data structures - List/Tuple/Dictionary
################
#LIST: similar to list of students in class room having Roll No & Name
list2 = [ '1','2','3','4']
list1 = [ "venu","kumar",3232,5445 ]
list3 = ['a','b','c','d' ]
print list1,list2,list3
#------------------
#ACCESSING THE LIST
#------------------
print list1[0] # venu
print list1[2:3] # [3232]
print list1[0:3] # ["venu","kumar",3232]
#------------------
#INSERTING/APPENDING/UPDATING/DELETING LIST
#------------------
#list1.insert('senthil') # TypeError: insert() takes exactly 2 arguments (1 given)
list1.insert(4,'senthil')
list1.append('muhthu')
print list1 # ['venu', 'kumar', 3232, 5445, 'senthil', 'muhthu']
print "---------"
list1.insert(4,5) # Here value "5" inserted into 4th index,but already existing 4th index "senthil" moved to 5th index
print list1
print list1[4],list1[5] # 5,senthil
print list3 + list2 # ['a', 'b', 'c', 'd', '1', '2', '3', '4']
#list1["x"] = 3 # TypeError: list indices must be integers, not str
list1[0] = 78 # while updating,existing element in same index moved to next one 
print list1 # [78, 'kumar', 3232, 5445, 5, 'senthil', 'muhthu']
del list1[0]
print list1 # ['kumar', 3232, 5445, 5, 'senthil', 'muhthu']
list1[0] = 0
print list1 # [0, 3232, 5445, 5, 'senthil', 'muhthu']
print "---------"
###################
###BASIC LIST OPERATIONS#####
##############
print len(list1) # 6
print list1 + list2 # [0, 3232, 5445, 5, 'senthil', 'muhthu', '1', '2', '3', '4']
print list1 * 4 # same list1 will repeat in 4 times with same order inside same list
#-------o/p below---
[0, 3232, 5445, 5, 'senthil', 'muhthu', 0, 3232, 5445, 5, 'senthil', 'muhthu', 0, 3232, 5445, 5, 'senthil', 'muhthu', 0, 3232, 5445, 5, 'senthil', 'muhthu']
#-----------------
print "3" in list1 # False
for x in list1: print x # 
#######o/p below ########
'''
0
3232
5445
5
senthil
muhthu '''
###################
#Indexing/Slicing/Metrices
###############
'''
index =    0    1    2     3 //positive count from LEFT
list =  [ '1', '2', '3',  '4']
index =   -4    -3  -2    -1   //Negative count from RIGHT
'''
###############
list = [ '1', '2', '3',  '4']
print list[1:] # [2,3,4]
print list[0:3] # [1,2,3] //excluding last index 
print list[1:3] # [2,3] // excluding last index 
print list[2:3] # [3] //Between 2 & 3,excluding last character
print "Built-In Functions"
###############
#Built-In Functions
#############
#CMP---MAX----MIN---LEN---LIST() ( for list to tuple conversion)
#############
#CMP( LARGER > SMALLER ) : o/p is 1 else -1,0 for both equal
#############
print "COMP() function"
#----------------------
list1 = [ '1', '2', '3']
list2 = [ '5','6','7']
list3 = ['a','b','c']
list4 = [ "hewhw","dsc","fds"]
list5 = [ '5','6','7']
list6 = ['A','B','C']
list7 = ['A','a',1,'$','%','&']
#----------------------
print cmp(list1,list2) # -1
print cmp(list2,list1) # 1
list3 = list2 + [675]
print list3 # ['5', '6', '7', 675]
print "Letters & numbers comp::",cmp(list3,list2) # 1
print "Letters & numbers comp::",cmp(list4,list3) # 1
print "Letters & numbers comp::",cmp(list3,list4) # 1
print cmp(list2,list5) # 0 ,since both are same
print cmp(list3,list6) # -1 ,since "A > a" but here its in reverse
print cmp(list6,list3) # 1 ,since "A > a" "A" has more value than "a"
###############"
#MAX() function
###############"
print " MAX() functions"
print "----------------"
print max(list1) # 3
print max(list3) # 7,since 7 is character but 675 is the number
print max(list4) # hewhw
print max(list6) # C
print max(list7) # "a" Max element from list of characters
###############"
#MIN() function
###############"
print " MIN() functions"
print "----------------"
print min(list1) # 1
print min(list3) # 675,since 7 is character but 675 is the number
print min(list4) # dsc
print min(list6) # A
print min(list7) # 1
##################
#list() function
############
#list() - To convert list to tuple
aTuple = (123, 'xyz', 'zara', 'abc');
#aList = list(aTuple)
#print "List elements : ", aList # [123, 'xyz', 'zara', 'abc']
################
##List Methods 
'''
append() - To add elements 
count() - Return counts of object
extend() -Append the contents of seq to list,l1.extend("abc"),then o/p is l1 = ['a','b','c'] 
index() - return index position of object
insert() - To insert the element
pop() - removes & returns last object from list
remove() - remove elements from list using its VALUE,but del() to remove using index
reverse() - To Reverse the list
sort() - To sort the list
'''

###############
#TUPLE....IMMUTABLE TYPE....ALWAYS HOLD STATIC DATA,like emp No/IP addr...DNS SERVER...IP ADDR/HOST NAME
##################
print "*************************"
print "TUPLES o/p"
tup = ('1','2')
tup2 = ('ab','cd')
print tup+tup2
#tup[0]=1 # TypeError: 'tuple' object does not support item assignment,since its IMMUTABLE type
#del tup = To delete the Tuple sequence completly
###############
###Basic Tuple operations
##############
'''
len(tup) # 2
tup+(2,3,4)
('2')*4 = (2,2,2,2)
3 in (1,2,3)
for x in (1,2,3): print x
'''
#########
L = ( 'a','b','c')
print L[2] # c
print L[-2] # b
print L[1:] # ('b','c')
##############
#ANY COMMA SEPERATED STRING WITHOUT () or {} or [] are set default to tuples
print 'a','b',432432
############
#CMP-->MAX-->MIN--->LEN---TUPLE
############
list2 = ['1','2','3']
print tuple(list2)
#############
# No Extra operations on tuple()
###########
#DICTIONARY ..>>English dictionary having Words & definitions,similarly here Key: Value concept
###########
'''
Not sequential access of elements from dict
Keys should be immutable types like string/Numbers (or) tuples
Values of any type
'''
###########
#ACCESSING/INSERTING/UPDATING/DELETING
########
dict = { "Name" : "venu","age":23,"mail":"vp@gmail.com",2:"rt"}
print dict['Name'] # "venu"
print dict['age'] # 23
print dict['mail'] # vp@gmail.com
dict['2'] = "muthu"
print dict # {'2': 'muthu', 'mail': 'vp@gmail.com', 'age': 23, 2: 'rt', 'Name': 'venu'}
###########
#DELETING
#############
del dict['Name'] # which will delete only that element
print "After deleting Name key",dict
dict.clear() # To clear all elements in dict,hence o/p is {} empty dictionary
print "After clear all elements",dict
del dict # Delete the dict completly
print "After deleting dict fully",dict # TypeError: 'type' object is unsubscriptable since its already deleted
##############
#Properties of Dict keys
##############
#No Duplicate keys are allowed,if so,last updated keys wins
res = { "id" : 324 ,"name":"venu","id":6655}
print res['id'] # o/p is 6655
#Keys are immutable type,you can use strings,tuples,numbers,but list is not allowed
dict = {'id':3,['j']:43}
print dict # TypeError: unhashable type: 'list'
#############
#Built-in directory functions & Methods
#############
cmp() - compare
len() - length
str() - string representation of dictionary
type() - returns type of passed variable
dict.clear() - To clear elements from dict
dict.copy() - Returns shallow copy of dict
dict.fromkeys() - Returns new dictionary with keys from seq & values set to value
dict.get(key,default=none) # For key,returns value
dict.has_key(key) # true
dict.items() # Returns list of dict(key,val) pairs
dict.keys() # Returns list of keys
dict.setdefault(key,default=None) # Similar to get,will set dict[key] = default,if its not there
dict.update(dict2) # add dict2 to dict
dict.values() # return values
#########
Examples
#########
dict1 = {'Name': 'Zara', 'Age': 7};
dict3 = {'id':'244343','place':'Mad'}
dict2 = dict1.copy()

print "New Dictinary : %s" %  str(dict2)
print "From keys",dict1.fromkeys('Age')
print "dict.get()",dict1.get('Age')
print "dict.has_key()",dict1.has_key('id')
print "dict.items()",dict1.items() # VERY USEFUL
print "dict.keys()",dict1.keys()
print "dict.setdefault()",dict1.setdefault('Age')
print "dict.update()",dict1.update(dict3)
print "dict.values()",dict1.values()
################
#o/p below
###############
#New Dictinary : {'Age': 7, 'Name': 'Zara'}
#From keys {'A': None, 'e': None, 'g': None}
#dict.get() 7
#dict.has_key() False
#dict.items() [('Age', 7), ('Name', 'Zara')]
#dict.keys() ['Age', 'Name']
#dict.setdefault() 7
#dict.update() {'Name': 'Zara', 'Age': 7,'id':'244343','place':'Mad'} 
#dict.values() [7, 'Mad', 'Zara', '244343']
######################
#####Interview Trick Questions#####
############

def myfun(val,mylist=[])
	mylist.append(val)
	return mylist

list1 = [ '10']
list2 = [123]
list3 = ['10','a']
print list1 
print list2
print list3
#########
Err o/p:  
---------
['10']
[123]
[10,a]

Actual o/p://Actually what happens is new default list is created only once when the function is defined, and that same list is then used subsequently whenever extendList is invoked without a list argument passed when calling this function,

This is because expressions in default arguments are calculated when the function is defined, not when it’s called.
No Default arguments invoked only once n used for further processing,how many called the same funtion untill pass ARG seperatly
-----------
['10','a']
[123]
[10,'a']
----------
In order to get above error o/p need to change code like below

def extendList(val, list=None):
  if list is None://if its none (or) Arg not passed,then need to declare New list every time to avoid same list appending
    list = []
  list.append(val)
  return list
#********************
def Multi():
	return [lambda x : i*x for i in range(4)] // range(4) means [0,1,2,3]
print [m(2) for m in Multi()]

#here calling Multi() function with arg value is 2 therefore lambda 2 : 0*2 = "0" , 2: 1*2 = "2" , 4 : 2*2 = "4", 6 : 3*2 = "6" hence [0,2,4,6] will be human error o/p
################
Err o/p:
[0,2,4,6]
Acutual o/p:
[6,6,6,6] due to LATE BINDING - during one time call itself,it will end with up with value of 3,since m(2) is passed,3*2 = 6 is printing all times means [3,3,3,3] * 2
The reason for this is that Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called.
------
More info:
when any of the functions returned by multipliers() are called, the value of i is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the for loop has completed and i is left with its final value of 3. 
###############
Tricky Questions
#############
List = [1,2,3,4]
print List[10:] = Empty list
print List[::2] = [2,4] print only even numbers
print List[::-1] = [4,3,2,1] Print in reverse order
###########
wrong answers
1. list = [ [ ] ] * 5 
2. list  # output? [ '5','5','5','5' ]
3. list[0].append(10)
4. list  # output? [ '510','520','5','5' ]
5. list[1].append(20)
6. list  # output?
7. list.append(30)
8. list  # output? [ '510','520','5','5','30']
########
Correct answers
1. list = [ [ ] ] * 5 
2. list  # output? [ [],[],[],[],[] ]
3. list[0].append(10)
4. list  # output? [ [10],[10],[10],[10],[10] ] // [] * 5 does NOT create a list containing 5 distinct lists; instead it will creates a list of 5 references to the same list,means 1 key with 5 references (i.e) list[0].
5. list[1].append(20) # [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]] //Similarly, list[1].append(20) appends 20 to the second list. But again, since all 5 lists refer to the same list, the output is now: 
6. list  # output?
7. list.append(30)
8. list  # output? [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20],30] //appending at end of entire list
########
tricky question -2
########
>>> list = [1,2,3,4]
>>> list[1].append[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'append'
>>>
#########
[1, 2, 3, 4, 5]
>>> list[1].append(6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'append'
>>> print list[1]
2
>>> print list[-1]
5
>>> print list[-1:]
[5]
>>> print list[-2:-1] # Excluding last character
[4]
>>> print list[-3:-1] # excluding last character
[3, 4]
############
     -4     -3     -2     -1   
[  1, 2,     3,     4,     5  ]
############

>>> print list[-1:-3]
[]
>>> print list[-1:-2]
[]
###############
tricky questions
#########
create list with Even numbers also its index should be even
        0 1 2 3 4  5  6  7  8
list = [1,3,5,8,10,13,18,36,78]
[x for x in list[::2] if x%2 == 0] // here list[::2] will access even indices
o/p is [10,18,78]
############
Given the following subclass of dictionary:

class DefaultDict(dict):
  def __missing__(self, key):
    return []
Will the code below work? Why or why not?

d = DefaultDict()
d['florp'] = 127 # o/p is { 'florp':127} it will work,since whenever a key is missing, the instance of the dictionary will automatically be instantiated with a list.
#################
http://www.python-course.eu/lambda.php - Lambda/map/reduce/filter
https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/ - Iterator/generator

############
All Types of  List operations from Python site
############
List Operations : append()/sort(re)/reverse()/extend(L)/remove()using value/insert()/pop()/index()/count()/
############
>>> L = [ 8,4,5,6,3]
>>> print L
[8, 4, 5, 6, 3]
>>> print L.append(9)
None
>>> L.append(9)
>>> print L
[8, 4, 5, 6, 3, 9, 9]
>>> L.remove(9)
>>> print L
[8, 4, 5, 6, 3, 9]
>>> L.extend(10) // need to pass list as input to extend
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> M = [2,3,4]
>>> L.extend(M)
>>> print M
[2, 3, 4]
>>> print L
[8, 4, 5, 6, 3, 9, 2, 3, 4]
>>> L.insert(3,17)
>>> print L
[8, 4, 5, 17, 6, 3, 9, 2, 3, 4]
>>> L.pop(3)
17
>>> print L
[8, 4, 5, 6, 3, 9, 2, 3, 4]
>>> L.index(6)
3
>>> L.count('3')
0
>>> L.count(3)
2
>>> print L.sort()
None
>>> print L
[2, 3, 3, 4, 4, 5, 6, 8, 9]
>>> print L.sort(reverse=True)
None
>>> print L
[9, 8, 6, 5, 4, 4, 3, 3, 2]
>>> print L.sort(key=3, reverse=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> L.reverse()
>>> print L
[2, 3, 3, 4, 4, 5, 6, 8, 9]
>>> L.reverse()
>>> print L
[9, 8, 6, 5, 4, 4, 3, 3, 2]
>>> M = L.copy()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'copy'
>>> print L[:]
[9, 8, 6, 5, 4, 4, 3, 3, 2]
>>> M = L[:]
>>> print M
[9, 8, 6, 5, 4, 4, 3, 3, 2]
>>> S = list(M)
>>> print S
[9, 8, 6, 5, 4, 4, 3, 3, 2]

Indexes: 
LTR =  0 to n
RTL = -1 to n 
Always LEFT to RIGHT concept same as STR indexes

>> L = [1,2,3,4]
>>> print L[-1]
4
>>> print L[-4]
1
>>> print L[-5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> print L[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>

LISTS AS STACK:
SyntaxError: invalid syntax
>>> L.append("H")
>>> print L
[9, 8, 6, 5, 4, 4, 3, 3, 2, 'H']
>>> L.pop()
'H'
>>> print L
[9, 8, 6, 5, 4, 4, 3, 3, 2]
>>>
Lists as Queue:
from collections import deque
queue = deque(L)
queue.append(‘H’)
queue.popleft() // remove first left most element as FCFS concept in Queue

List as comprehensions:

writing single line of code

[ (X) for X in L] - X is item in list and perform operations of each item in list
[ (x**2) for X in L] 

>>> [ (x**2) for X in L]
[4, 4, 4, 4]

>>> print L
[9, 8, 6, 5, 4, 4, 3, 3, 2]
>>> squares = [x**2 for x in L]
>>> print squares
[81, 64, 36, 25, 16, 16, 9, 9, 4]
—————
>>> res = list(map(lambda X : X+1, L))
>>> print res
[2, 3, 4, 5]
>>>
>>> X = [1,2,3]
>>> Y = [4,5,6]
>>> [ (x,y) for x in X for y in Y if x!=y]
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)] similar to list.append((x,y))
———————
>>> X = ['A','B','C']
>>> Y = ['a','b','c']
>>> [(x,y) for x in X for y in Y if x.lower() == y]
[('A', 'a'), ('B', 'b'), ('C', 'c')]
>>>

Applying functions on elements of list:
>>> L = [1.2,3,9.0]
>>> [ abs(x) for x in L]
[1.2, 3, 9.0]
>>> [ int(x) for x in L]
[1, 3, 9]
>>> [ float(x) for x in L]
[1.2, 3.0, 9.0]
>>> [ oct(x) for x

Calling method on elements on List:
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>>

Creating list of 2 tuples like 
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]


matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]

>>> [row[2] for row in matrix] // printing 3rd columns values
[3, 7, 11]
>>> [row[0] for row in matrix]
[1, 5, 9]
>>>
using  [row[2] for row in matrix] logic, pulling all columns elements one by one n insert into another list
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

list(zip(*matrix)) // will do same operations quickly
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

DEL statement:
del will delete both indices & values
>>> print L
[1.2, 3, 3, 5, 6]
>>> del L[-1:-2]  Always LTR deletion same as indices,not in reverse
>>> print L
[1.2, 3, 3, 5, 6]
>>> del L[-2:-1]

REMOVE statement : To remove element by its value
if duplicate elements r there,then it will remove first occurrence of value

>>>print L
[1.2, 3, 6, 3]
>>> L.remove(3)
>>> print L
[1.2, 6, 3]
>>>
#################
TUPLES:
#################
>>> t = hello,venu,world
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined

String default data type is tuple
>>> t = 'hello,venu,world'
>>> print t
hello,venu,world

>>> t = 'hello','venu','world'
>>> print t
('hello', 'venu', 'world')

>>> u = t,(1,2,3,4) adding 2 tuples together
>>> print u
(('hello', 'venu', 'world'), (1, 2, 3, 4))

IMMUTABLE types:

>>> t[0] = 345
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment 

Accept mutable objects:

>>> L1 = [1,2,3]
>>> L2 = [3,4,5]
>>> v = (L1,L2)
>>> print v

([1, 2, 3], [3, 4, 5])
>>> x = ()
>>> print x
()
>>> len(x)
0
String here:
>>> name = "sakthi"
>>> len(name)
6
>>> print name
sakthi

Converted to tuple using trailing Comma at end:

>>> name = "sakthi",
>>> len(name)
1
>>> print name
('sakthi',)

>>> print v
([1, 2, 3], [3, 4, 5])
>>>

>>> i,j,k = v
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: need more than 2 values to unpack // here V contains only 2 values but LFH assignment having 3 values i,j,k

>>> print t
('hello', 'venu', 'world')

>>> i,j,k = t
>>> print i
hello
>>> print j
venu
>>>
##############
SETS
############
Sets:

>>> emp = { 'x','y','z'}
>>> print(emp)
set(['y', 'x', 'z'])

>>> name = "venu"
>>> print set(name)
set(['u', 'n', 'e', 'v'])

Basic set operations also included:

a - b // a & b // a | b ( basic set operations)


Remove Duplicates:

>>> emp = { 'x','y','z','x','y'}

>>> print(emp)
set(['y', 'x', 'z'])
>>>
#################
DICTIONARIES
################
KEYS - ACCEPTS ONLY IMMUTABLE OBJECTS like Strings,numbers & tuples ( if tuples contains any mutable object,then it can't be used)

1.Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. 
2.Unlike sequences, which are indexed by a range of numbers, 
3.dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. 
4.Tuples can be used as keys if they contain only strings, numbers, or tuples; 
5.if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
6.You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

OPERATIONS on DICT()
>>> tel = {'jack': 4098, 'sape': 4139}
ADDING:
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']
4098

DELETION:
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}

PRINT ONLY KEYS:

>>> list(tel.keys())
['irv', 'guido', 'jack']
>>> sorted(tel.keys())
['guido', 'irv', 'jack']

MEMBERSHIP:

>>> 'guido' in tel
True
>>> 'jack' not in tel
False
------------
DICT creation from LIST (or) TUPLE
------------

dict(list) # where list contains tuples

>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}

>>> dict(('sape', 4139), ('guido', 4127), ('jack', 4098))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: dict expected at most 1 arguments, got 3

>>> dict((('sape', 4139), ('guido', 4127), ('jack', 4098)))
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>>

LIST & TUPLE TO DICT CONVERSION END UP WITH ERROR:
need key/value for this conversion

>>> L = [1,2,3,4]
>>> print dict(L)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> L = (1,2,3,4)
>>> print dict(L)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>>
------------
We can create dict from dict comprehension
>>> {x: x**2 for x in range(4)}
{0: 0, 1: 1, 2: 4, 3: 9}
--------Dict direct creation using strings
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>>

COMBINING 2 LISTS into single DICTIONARY

L1 = ['x','y','z']
L2 = [1,2,3]
for k,v in zip(L1,L2):
	print (k,v)
>>> L1 = ['x','y','z']
>>> L2 = [1,2,3]
>>> for k,v in zip(L1,L2):
...         print (k,v)
...
('x', 1)
('y', 2)
('z', 3)
>>>
#############
GENERAL COMPARISON

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

