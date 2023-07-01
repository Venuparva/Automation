
import os

a=2+2
b=2*2-3
c=5-2/3+4
d=4.7-3.4/2.3
e=3.2/3.2
f=9/2.5
g=15%3
h=17//3 # discards the fractional part
i=2**3
#j=2***3 # syntax error
k=2
l=3*4
m=k*l
#n # NameError: name 'n' is not defined,variabele should be assigned before usage
#print m + _ ( _ contains old saved value while using in python interruptor
n=3+7j
o=5-4j
print "--------"
print a,b,c,d,e,f,g,h,i,k,l,m,n,o
#o/p value:
#4 1 9 3.22173913043 1.0 3.6 0 5 8 2 12 24 (3+7j) (5-4j)
#(8+3j)
print n+o
"""
#####################
Operator precedence short cuts to memorize : PUPMDM+-RLB&|^(CMP/E/AS)ISINNOTorand
#####################
Operator	Description
**	Exponentiation (raise to the power)
~ + -	Ccomplement, unary plus and minus (method names for the last two are +@ and -@)
* / % //	Multiply, divide, modulo and floor division
+ -	Addition and subtraction
>> <<	Right and left bitwise shift
&	Bitwise 'AND'td>
^ |	Bitwise exclusive `OR' and regular `OR'
<= < > >=	Comparison operators
<> == !=	Equality operators
= %= /= //= -= += *= **=	Assignment operators
is is not	Identity operators
in not in	Membership operators
not or and	Logical operators
"""
#############
#Tricky interview qns
###########
def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)
    
def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)

div1(5,2) 
div1(5.,2)
div2(5,2)
div2(5.,2.)
############
python-2 o/p
############
5/2 = 2
5.0/2 = 2.5
5//2 = 2 
5.0//2.0 = 2.0 ( (//) operator will always perform integer division, regardless of the operand types)
############
Python-3 o/p
#########
5/2 = 2.5
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
##########

