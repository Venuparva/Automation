import string
print 'helo world'
#Both """ (or) ''' used for big paragraph (or) script inside script,very powerful tool
#print 'don't know' # SyntaxError: invalid syntax,since its already closed
print "don't know"
print 'don\'t know'
#print 'don\\'t know' # SyntaxError: invalid syntax
print '\don\\\'t know'
print 'my name is "venu" '
print '"yes",he said'
print '\"yes\",he said'
print 'first line\nsecondline'
all_symbols = ''' #~!@#$%^&*()_+=-{}|\:;"'[]?/><.,` '''
print all_symbols
print "venu.parve@gmail.com"
print "hdash\\ndakdn"
print r"hdash\\ndakdn" # using r at the beginning make \ as its raw string o/p in this line is hdash\\ndakdn
print "---------"
print """\
ndkasd
dasdkj
"""
print "venu is grea" + 10*"t" # venu is greatttttttttt
print "ven" "usakthi" # venusakthi
print 'ven' 'usakthi' # venusakthi
var = "hello"
#print var "world" # it will end up with syntax error
print var+"world" # hello world
text = ('dewbdioewdjbewdb'
'bweubuewbyewhiewoh')
print text # o/p is dewbdioewdjbewdbbweubuewbyewhiewoh
##########
#indexing & slicing
##########
#General tips : LF to RT : 0,1,2.....
#RT to lf : -1,-2....
word = 'python'
#LTR
print word[0] # p
print word[1] # y
print word[2] # t
print word[5] # n
#RTL
print word[-1] # n
print word[-2] # o
print word[-3] # h
print word[-6] # p
"""
------------------
0   1   2  3  4  5
------------------
p   y   t  h  o  n
------------------
-6  -5  -4 -3  -2 -1
"""
print "#######Slicing logic below#########"
#Slicing:
#Slicing logic will used to get substring of it
print word[0:2] # py
print word[2:0] # empty string
print word[:2] # py
print word[2:] # thon
print word[:] # python
#print word[] # syntax error
print "#######Slicling negative values######"
print word[-1:0] # Empty values not in proper order,hence empty
print word[0:-1] # pytho
print word[-1:-3] # Empty values not in proper order,hence empty
print word[1:0] # Empty values not in proper order,hence empty
print word[0:1] # p
print "valeu",word[0:1:2]# p
print "valeu",word[3:4:5]# h
print "valeu-3",word[0:3:5]# p
print "valeu-4",word[0:1:2]# p
print "-----*******------"
######################
#SLICING LOGIC below
"""
--------------------------------------
0     1       2      3     4      5     6
---------------------------------------
|  p  |    y  |   t  |  h  |   o  |  n  |
---------------------------------------
-6    -5     -4     -3    -2     -1    
---------------------------------------
#Note : Length of slice is difference of indices,example word[1:3] = 3-1 =2 = "yt"
"""
#print word[43] # Index error : out of range
print word[3:43] # 'hon' print from 3 indices to 43,hence o/p is 'hon'
print word[43:] # prints empty string
########STRINGS ARE IMMUTABLE#######
print "---------"
#Note : String are IMMUTABLE,replacement using index is not possible
#word[0] = "T" # TypeError: 'str' object does not support item assignment
print "T"+word[1:6] # o/p is "Tython"
#o/p for above code below
print word[:2] + "py" # o/p is pypy
s = 'he   wd' #here 2 space,hence total = 7
s = 'he wd' # space 1,hence total = 5
print len(s) # Here including space,total length is 5

#######################
# Unicode Strings
#######################
print u'Hello world' # unicode mode - to handle unicode characters 0 to 256 # o/p is Hello world
print u'Hello\u0030world !' # Hello0world ! unicode provide access to all registered unicode codecs ( coders & decoders)
print ur'Hello\\u0030world !' # unicode -raw mode (ur) used to print lot of blackslashes Hello\\u0030world !
print ur'Hello\\\u0030world !' # Hello\\0world !
print u"abc"
print str(u"abc")
###############################
Escape sequence:
###############################
\b = backspace
\n = new line
\t = Tab
\s = Space
\x = Character
##############################
Special operators:
##############################
(+) Concatenation
(*) Repitation
[ ]-Slice
[:] - Range slice
in - Membership
not in - membership
r/R - Raw string # print r'\n'
% - String formator
print """ %d given name is %s """%("1,"venu") # 1 given name is venu,old version
print """ {0} given name is {1} """.format("1","venu") # 1 given name is venu ,latest python version
##############################
Formating string
##############################
%c - character
%s - string
%f - float
%d - int
%x - hexadecimel
* - Argument specified width
(-) - Left justification
+ - display sign
<sp> - space after + number
m.n - m- minimum total width & n- number of decimal points to display after dot (.)
print 'C:\\nowhere'  # C;\nohwere
print r'C:\\nowhere'  # Notice "r" raw string in it, C;\\nohwere
##############################
Built-in String methods
##############################
x = "venu sakthi"
(1) Capitalize - Capitalize first character  # o/p is Venu sakthi
(2) center(width,fillchar) - print str.center(40, 'a') # venuaasakthi,fill all the values with 'a'
(3) count() - count occurances - count("v",0,len(x)) # 1
(4) decode/encode - str.decode('base64',x)
(5) startswith/endswith - x.endswidth("thi") o/p is TRUE for both x.startswith("ve")
x = "venu\tsakthi"
(6) expandtabs() - x.expandtabs(8) default is 8 # venu           sakthi
(7) find/index - return index if found,orelse -1 # index() - return if index,not raise exception
(8) is:
		|-isalnum() - True for "this2009" # conatins both numbers & characters only
		|-isalpha() - True only if "this",no numbers r spaces accepted
		|-isdigit() - True only if "632762" ,false otherwise
         (is) --|-islower() - True only if "venu" all small letters
		|-isnumeric() - same as isdigit() but applicable on unicode, u'this2009' (notice "u" in front)- True
		|-isspace() - Only whitespce in string including 1 charac,otherwise false
                |-istitle() - "Venu Sakthi Is Good Boy" - True
                |-isupper() - "VENU SAKTHI" - True, All r upper case letters
(9)join(seq) - join all characters (or) merge into string
(10) len(x) - Length of string
(11)ljust() # to fill rest of spaces with some characters x.ljsut(20,"0") # venu sakthi000000000000000
(12) "VENUSAKTHI".lower() - "venusakthi"
(13) lstrip/rstrip/strip - left space/right space/ space
(14)maketrans() - VERY POWERFUL FUN - replace intab with outab
----------------------
Example: maketrans()
----------------------
x= "venu sakthi"
intab = "vaki"
outab = "1234"
from string import maketrans
res = maketrans(intab,outab)
print x.translate(res) # pass the format to string # o/p is "1enu s23hi" //replace all intab character with outab ones
----------------------
(15) max("tree") # last abcd character from string "tree",here "t" XYZ --->T ---> ABCD
(16) min("venu") # first abcd character from string "venu",here "e",ABCD---> E--->XYZ
(17) ("cattaanneae").replace("a","x",3) # o/p is cxttx/anneae --here only first & second "a"'s getting replaced,since 3 is given
#suppose 3 is not given then all "a" is replaced with "x"
(18) x.rfind("a") # search the string in reverse() # returns position of string in reverse way
(19) x.rindex("a") # search the string in reverse() # returns index of string
(20)x.rjust(50,"Y") # "YYYYYYYYYYYYYYYYYVENU SAKTHI"
-----------------
RFIND/RINDEX/RJUST
-----------------
(21)SPLIT- Split String based on delimiter,space by default
(22)SPLITLINES - Split string based on \n new lines
(23)swapcase() - Lower to Upper,upper to lower
(24)startswith()
(25)title() - "Venu Sakthi Is Good Boy"
(26)translate() - used in maketranslate function,refer that
(27)upper() - Converts lower to upper case
(28) zfill() - Fills left side with zero's x.zfill(10) # "000000000000000VENU SAKTHi"
########OUTPUT BELOW########
"""
helo world
don't know
don't know
\don\'t know
my name is "venu"
"yes",he said
"yes",he said
first line
secondline
 #~!@#$%^&*()_+=-{}|\:;"'[]?/><.,`
venu.parve@gmail.com
hdash\ndakdn
hdash\\ndakdn
---------
ndkasd
dasdkj

venu is greatttttttttt
venusakthi
venusakthi
helloworld
dewbdioewdjbewdbbweubuewbyewhiewoh
p
y
t
n
n
o
h
p
#######Slicing logic below#########
py

py
thon
python
#######Slicling negative values######

pytho


p
valeu p
valeu h
valeu-3 p
valeu-4 p
-----*******------
hon

---------
Tython
pypy
5
Hello world
Hello0world !
Hello\\u0030world !
Hello\\0world !
abc
abc

"""
#have to cover this as well https://docs.python.org/2/library/stdtypes.html#typesseq
