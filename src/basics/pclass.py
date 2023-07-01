#!/usr/bin/python

class Employee: # class name
   'Common base class for all employees' # Documentation string
   cempCount = 0 # class variable
   csalary = 0
   age = 0

#Constructor
   def __init__(self, name, salary): # class constructor (or) initialization method that python calls when you create new instance of class
      self.name = name
      self.salary = salary
      Employee.cempCount += 1
      Employee.csalary = Employee.csalary + salary
   
   def displayCount(self):
     print "Total Employee %d" % Employee.cempCount

   def displayEmployee(self):
      print "Parent class Name : ", self.name,  ", Salary: ", self.salary
      print "Name : ", self.name,  ", Parent class Age: ", self.age

   def print_total_salary(self):
      print "total salary",Employee.csalary

"This would create first object of Employee class"
# instance (or) object creations:
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp3 = Employee("venu", 1000)
#emp4 = Employee() # it will throw error like TypeError: __init__() takes exactly 3 arguments (1 given)

# accessing the class attributes 
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp3.print_total_salary()
print "Total Employee %d" % Employee.cempCount

#Adding/updating/deleting attributes
emp1.age = 7
emp2.age = 8
emp3.age = 18

#functions to accessing attributes
#hasattr,getattr,setattr,delattr
print hasattr(emp1,'name')
print getattr(emp1,'name')
print setattr(emp1,'name','muthu')
emp1.displayEmployee()
print delattr(emp1,'name')
#emp1.displayEmployee() # will throw error,since its already deleted

print "==========="
#Built-in class attributes:
#doc/dict/name/module/bases
print Employee.__doc__ # documentation string for class purpose definition, none if undefined 
print Employee.__name__ # Class name.
print Employee.__module__ # Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print Employee.__bases__ # A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.suppose class A delcared inside class Employee,then it will list in order as Employee & A...
print Employee.__dict__ # Dictionary containing the class's namespace.


print "==========="
#Destructor:
emp5 = emp1
print id(emp5)
del(emp1)
#print id(emp1)
#print id(emp4)  # Error : NameError: name 'emp4' is not defined

#inheritance concept
class Manager(Employee):
 	name = 'mani'
        age = 55
        salary = 12345
	"Manager class inherits employee parents class"
	def __init__(self,name,age):
        	cname = self.name # AttributeError: Manager instance has no attribute 'name',if name is not declared under Manager class
                cage = self.age
                print "child construct values",cname,cage
	def child_class(self,name,age):
   		print "child class Name & Age::",self.name,self.age
print "==========="
mgr1 = Manager("senthil",24)
print "########################"
#CASE-1:: o/p without constructor & variables inside child Manager class:
print "o/p-1",mgr1.child_class("vadivel",45)
	#child class Name & Age:: senthil 0
	#None
print "o/p-2",mgr1.displayEmployee()
	#Parent class Name :  senthil , Salary:  24
	#Name :  senthil , Parent class Age:  0
	#None
print "########################"
#CASE-1:: o/p with constructor & variables inside child Manager class:
print "o/p-1",mgr1.child_class("vadivel",45)
	#child construct values mani 55
	#o/p-1 child class Name & Age:: mani 55
	#None
print "o/p-2",mgr1.displayEmployee()
	#o/p-2 Parent class Name :  mani , Salary:  12345
	#Name :  mani , Parent class Age:  55
	#None
print setattr(mgr1,'name','jack')
	#None
print "########################"
#mgr1 = Manager() # Error - TypeError: __init__() takes exactly 3 arguments (1 given),In order to avoid this,we need to declare contructor inside Manager class with 3 arguments like __init__(self,name,age) self.name = "lakshsmi",self.age=56,then it will work 
#print mgr1.displayEmployee("Kumar",30) # Error - TypeError: displayEmployee() takes exactly 1 argument (3 given),here trying to function overloading concept
#print "child class values printing-1::",mgr1.child_class() # Error - TypeError: child_class() takes exactly 3 arguments (1 given),In order to avoid this,we need to declare contructor inside Manager class ,then it will print senthil,24



#class A:        # define your class A
#.....

#class B:         # define your calss B
#.....

#class C(A, B):   # subclass of A and B
#.....
#You can use issubclass() or isinstance() functions to check a relationships of two classes and instances.
#The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.
#The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class

print "**********"
#Basic OVER RIDING Methods:

#You can always override your parent class methods. One reason for overriding parent's methods is because you may want special or different functionality in your subclass.
class parent():# define parent class
	def add(self):
		print "parent add"
class Child(parent):# define child class
	def add(self):
		print "child add"
c = Child()
p = parent()
#print c.add() # TypeError: add() takes no arguments (1 given),without self given as argument inside add() function
print c.add()
	#child add
 	#None
print p.add()
	#parent add
	#None

print "**********"
#Base Overloading Methods
#__init__ : constructor call by "c = Child()"
#__del__: destructor call by "del c"
#__repr__: call by repr(c)

print str(c) # <__main__.Child instance at 0x10f34f758> Printable string representation
print repr(c) # <__main__.Child instance at 0x10f34f758> Evaluatable string representation
print cmp(c,p) # -1 Object comparison
x = "venu"
print x.__repr__() # 'venu'
print x.__str__() # venu
#print eval(x) #NameError name venu is not defined

#Operator loading:
class Point:
    # previous definitions...
    def __init__(self,x = 0,y = 0):
       self.x = x
       self.y = y
    # without below function,it wont display proper values ,<__main__.Point instance at 0x10198acf8>,string formatting function
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2) # o/p is (1,5) # What actually happens is that, when you do p1 + p2, Python will call p1.__add__(p2) which in turn is Point.__add__(p1,p2). 

Similarly few more:

Addition	p1 + p2	p1.__add__(p2)
Subtraction	p1 - p2	p1.__sub__(p2)
Multiplication	p1 * p2	p1.__mul__(p2)
Power	p1 ** p2	p1.__pow__(p2)
#-------------------------
#Function overloading:
#------------------------

class A(object):  # Remember the ``object`` bit when working in Python 2.x

    def stackoverflow(self, i=None):
        if i is None:
            print 'first form'
        else:
            print 'second form'

ob = A()
ob.stackoverflow() # first form,default None value is taken here and also if condition becomes true
ob.stackoverflow(2) # second form,user given 2 is taken and also else condition becomes true


#Data Hiding
# An object's attributes may or may not be visible outside the class definition. You need to name attributes with a double underscore prefix, and those attributes then are not be directly visible to outsiders.

#!/usr/bin/python

class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count() # 1
counter.count() # 2
#print counter.__secretCount # AttributeError JustCounter instance has no attribute __secretCount in order to access ituse like below
print counter._JustCounter__secretCount # 2 


COMPLETE o/p of above code:

Venu:python_tips venu$ python pclass.py
Parent class Name :  Zara , Salary:  2000
Name :  Zara , Parent class Age:  0
Parent class Name :  Manni , Salary:  5000
Name :  Manni , Parent class Age:  0
Parent class Name :  venu , Salary:  1000
Name :  venu , Parent class Age:  0
total salary 8000
Total Employee 3
True
Zara
None
Parent class Name :  muthu , Salary:  2000
Name :  muthu , Parent class Age:  7
None
===========
Common base class for all employees
Employee
__main__
()
{'csalary': 8000, 'displayCount': <function displayCount at 0x104cd0230>, 'displayEmployee': <function displayEmployee at 0x104cd0938>, 'age': 0, '__module__': '__main__', 'print_total_salary': <function print_total_salary at 0x104cd47d0>, 'cempCount': 3, '__doc__': 'Common base class for all employees', '__init__': <function __init__ at 0x104cc7b90>}
===========
4375599728
===========
child construct values mani 55
########################
o/p-1 child class Name & Age:: mani 55
None
o/p-2 Parent class Name :  mani , Salary:  12345
Name :  mani , Parent class Age:  55
None
########################
o/p-1 child class Name & Age:: mani 55
None
o/p-2 Parent class Name :  mani , Salary:  12345
Name :  mani , Parent class Age:  55
None
None
########################
**********
child add
None
parent add
None
**********
<__main__.Child instance at 0x104ce5c20>
<__main__.Child instance at 0x104ce5c20>
-1
'venu'
venu
(1,5)
first form
second form
1
2
2

# Python website details below dos.python.org

#Python classes provide all the standard features of Object Oriented Programming:
#1.the class inheritance mechanism allows multiple base classes, 
#2.a derived class can override any methods of its base class or classes, and 
#3.a method can call the method of a base class with the same name.
#4.classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.
# and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples)
#5.aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types. This is usually used to the benefit of the program, since aliases behave like pointers in some respect

# Namespace: 
class A()
	a =5
objA = A()
objA.a = 3 // a is attribute and storing 3 to  objA is namespace is a mapping from names to object,The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted.The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function

#Scope :

#Although scopes are determined statically, they are used dynamically. At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:

#the innermost scope, which is searched first, contains the local names
#the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
#the next-to-last scope contains the current module’s global names
#the outermost scope (searched last) is the namespace containing built-in names


#x = MyClass() // class instantiation automatically invokes __init__() for the newly-created class instance x
# the special thing about methods is that the object is passed as the first argument of the function. In our example, the call x.f() is exactly equivalent to MyClass.f(x).


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
#Methods may call other methods by using method attributes of the self argument:
Example below:
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

#Below also possible

class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

Here are naming conventions for Python identifiers −

Class names start with an uppercase letter. All other identifiers start with a lowercase letter.

Starting an identifier with a single leading underscore indicates that the identifier is private.

Starting an identifier with two leading underscores indicates a strongly private identifier.

If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.
################
##Tricky questions
############
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x # 1,1,1 # Both child's inherits parent ,so 1,1,1
Child1.x = 2
print Parent.x, Child1.x, Child2.x # 1,2,1 correct o/p is 1,2,1, since change happend at one child level in previous line won't affect both parent + another child as well 
Parent.x = 3
print Parent.x, Child1.x, Child2.x # 3,1,1 correct o/p is 3,2,3,Here change happend at parent level ,hence it should affect all of its children,so parent giving option to his both kids C1 & C2 regarding update,but its child option to accept it,since child2 didn't have any change like child2.x = 5 outside,it value changed to 3,but child1.x = 2 is declared under print stmt,it values remains same,(i.e) Child1 telling to dad "Hello dad... I don't need your updated option..will remains with my value only i.e child1.x = 2",so its 3,2,3

Note: Suppose ,if I declare child2.x = 5 lets c how its behaves
See below here child2 also rejected dad option of parent.x = 3 
>>> Child2.x = 5
>>> print Parent.x, Child1.x, Child2.x
3 2 5
########
Few more cases for above pgm

                         Parent1 ( x = 3 )
             ______________|  
   (x=2)   Child1          Child2 ( x = 3 ) ,but Child2.x = 5 means then (x =5),again changing value to (x=8)
                           |
                         Child3 ( x = 7) so, 3,2,5,7 is o/p
 			   |
			 Child4 (3,2,8,7),Now Im changing value in parent x=3,then o/p is (9,2,8,7)
			   | 
			 Child5 # simply pass is there,hence (9,2,8,7,7) is final o/p,so it wont refer grand parent ,will follow its immediate parent only

>>> class Child3(Child2):
...     pass
...
>>> Child3.x = 7
>>> print Parent.x, Child1.x, Child2.x,Child3.x
3 2 5 7
>>> Child2.x = 8
>>> print Parent.x, Child1.x, Child2.x,Child3.x
3 2 8 7
>>> Parent.x = 9
>>> print Parent.x, Child1.x, Child2.x,Child3.x
9 2 8 7
>>> class Child4(Child3):
...     pass
...
>>> print Parent.x, Child1.x, Child2.x,Child3.x,Child4.x
9 2 8 7 7
>>> class Child5(Child4):
...     pass
...
>>> print Parent.x, Child1.x, Child2.x,Child3.x,Child4.x,Child5.x
9 2 8 7 7 7
>>> Parent.x = 10
>>> print Parent.x, Child1.x, Child2.x,Child3.x,Child4.x,Child5.x
10 2 8 7 7 7
>>> Child3.x = 11
>>> print Parent.x, Child1.x, Child2.x,Child3.x,Child4.x,Child5.x
10 2 8 11 11 11
>>>
################################
###General Tips of OOPS inheritance
################################

# Value changed at Child Level ,wont affect its parent level values
# Value chnaged at parent level,will affect all of its immediate children,but its childrent option to accept it (or) not
