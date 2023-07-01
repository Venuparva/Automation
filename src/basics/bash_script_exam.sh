#!/bin/bash

############
pwd
ls
var="/tmp" # _ALI,TOKEN_A,VAR_1 are invalid
############
#LOCAL_Variable 
#Environ_variable
#Shell Variables
############
echo "--------------"
echo "Sample Bash scripting"
echo "--------------"
read input
echo "o/p here",$input
echo "variable o/p here",$var
unset var
echo "variable o/p here",$var
############
#Special variables
############
#  $0 - filename of script
#  $# - Number of arguments
#  $n - corresponding variables ( $1,$2...)
#  $* - All Arugments are double quoted,if script receives 2 arguments $* = $1,$2
#  $@ - All Arugments are INDIVIDUALLY double quoted,if script receives 2 arguments $* = $1,$2
#  $? - Exit status of previous command success (or) failure status
#  $$ - Process number of current shell,Process ID under which they r executing
#  $! - Process number of last background command
############
#example:
#for TOKEN in $*
#do
#   echo $TOKEN
#done
#------------
#./test.sh venu sak 25 old
#venu
#sak
#25
#old
#############
#ARRAY:
#array_name[index]=value //syntax
emp_list[0]="Arun"
emp_list[1]="venu"

echo "Array 0th element is",${emp_list[0]}
echo "Array 1st element is",${emp_list[1]}
#------------
for item in "${emp_list[*]}"
do
	echo $item
done
#---------
a=2
b=3
c=`expr $a+$b`
#echo $c # o/p is 2+3
c=`expr $a + $b`
echo $c # o/p is 5 // Need to give space inside expression
tee local << EOF 
###############
Arthimetic operations
###############
+ -> c=`expr $a + $b`
* -> c=`expr $a * $b`
- sub
% Mod
/ Div
= ->  a=$b // To assign the variable value to another one
== Equality testing  [ $a == $b ] returns True else false//SPACES is IMPORTANT neat Brackets
!= Not Equal
##############
Relational Operators
##############
a=10
b=5
#Spaces are very important
if [ $a -eq $b ] // returns false //Equals
if [ $a -ne $b ] // returns false // Not Equals
if [ $a -gt $b ] // returns false // Greater than
if [ $a -lt $b ] // returns false // Less than
if [ $a -ge $b ] // returns false // Greater than (or) Equal
if [ $a -le $b ] // returns false // Less than (or) Equal
################
Boolean Operators
################
[! false] - NOT
-o - OR [ [ $a -gt $b ] -o [$b -lt $c ] -a [$a < 3] ]
-a - AND
#############
STRING Operators
#############
a="abc"
b="efg"
--------
= checks both values of 2 operands r correct [ $a = $b ] // not true
!= Not Equal check
-z = check if given string operand size is zero [ -z $a ]
-n = check if given string operand size is non-zero [ -n $a ]
str = check if the string is not empty [ $a ]  # o/p is True
#########
#File Operations
#########
[ -d file ] # check if file is directory
[ -f file ] # check if file is ordinary file
[ -x file ] # check if file is executable
[ -s file ] # check if file size > 0
[ -e file ] # check if file exists
###############
if [ exp ] 
then
	stmt
elif [  ]
then
	stmt
else
	stmt
fi
###############
while [ "$a" -lt 9 ] // similar to until just replace while with until
do
	if [ "$a" -eq 4 ]
	break/continue
     stmt	
done
#############
for i in str // similar to for use select var in word:
do
	echo $i
done
#############
case word in
	pattern1)
		stmt
	;;
	pattern2)
		stmt
	;;
esac
##############
#break() & Continue() - Statements are same as python
############
a=10
echo -e "value of a is $a \n" # o/p is "Value of a is 10 \n"
echo  "value of a is $a \n" # o/p is "Value of a is 10"
##########
DATE=`date`
echo "Date is $DATE"
USERS=`who | wc -l`
echo "Users count is $USERS"
##########
#${var} = Substitute the value of var
#${var:-word} = if var is NUll r unset ,then word is substituted for var ,lllr to var=word
#${var:=word} = var is set to value of word lllr to var=word
#${var:?message} = message is printed to standard error 
#${var:+word} = similar to var=word
#########
#single quotes - ' ' = All special characters between these quotes lose their special meaning.
#double quotes - " " = Most special characters between these quotes lose their special meaning with these exceptions
#EXCEPT BELOW:
#$
#`
#\$
#\'
#\"
#\\
#Backslash - Any character immediatly following these loses its special character
#Back quote - ` ` - All are execueted as UNIX commands
##########
EOF
var=50
echo \<h\>HTML HEADING \<\/h\>
echo "the dollar value is $var" # the dollar value is 50
echo "the dollar '$'value is $var" # the dollar '$'value is 50
echo "the dollar \$ value is $var" # the dollar $ value is 50

VAR=ZARA
echo '$VAR owes <-$1500.**>; [ as of (`date +%m/%d`) ]'
echo "$VAR owes <-$1500.**>; [ as of (`date +%m/%d`) ]" # ZARA owes <-500.**>; [ as of (06/12) ]
echo "it\'s shell pgm" # it\'s shell pgm
echo "it's shell pgm" # it's shell pgm
#############

who > users
#echo hello > users
#echo line 1 > Users
`cat /Users/venu 1/Documents/python_tips/users`
> file redirection
>> file appending
###########
Here doc
cat << EOF
kdaskcadnsjcnasdkjnas
EOF
cat /tmp/sak.txt << EOF
kdaskcadnsjcnasdsdskjnas
EOF
############
#Discard the o/p
echo "------o/p-1------------"
#`cat /tmp/venu` > /dev/null #End up with Error quotes(`) should come at the end
echo "--------o/p-2----------"
`cat /tmp/venu > /dev/null` # No such file (o) directory
echo "--------o/p-3----------"
`cat /tmp/venu > /dev/null 2>&1` #o/p is empty ,since its already redirected 1-STDOUT & 2-STDERR
echo "---------o/p-4---------"
`cat /tmp/venu > /dev/null 1>&2` # 1,2  to display o/p ,reverse is empty
#----------------------
cat << EOF
pgm > file # file redirection
pgm < file # file input reading
pgm >> file # file appending
pgm << file # HERE DOC
#----------------------
0 = STDIN
1 = STDOUT
2 = STDERR
#----------------------
n > file # file input reading
n >> file # file input reading
n >& m # Merge o/p from stream n with stream m
n <& m # Merge i/p from stream n with stream m
<< tag # file input reading
| # takes output from one prgm
EOF
#-------------
add() {
echo "adding"
return 1
}
add()
#----------------------
# you can call the function from prompt() also
#just call function add() from command line ,which will work
#unset .f add() //remove definition of fun() from shell
#----------------------
# SED - s/pattern/p - print the line
# SED - s/pattern/d - delete the line
# SED - s/pattern1/pattern2/g - substitue the line
#Example 
#######
#cat /etc/pwd
line -1 : first line
line -2 : second line
line -3 : third line
line -4 : foruth line
line -5 : fifth line
line -6 : sixth line
line -7 : seventh line
line -8 : eight line
#######
#cat file | sed 's/hello/world/g'
#sed -e 'd' /etc/pwd - To delete all lines
#o/p is empty
#sed -e '1d' /etc/pwd - To delete first line from file
o/p is 7 lines except first line
#sed -e '1, 5d' /etc/pwd - To delete 1 to 5th line in file ,sed won't work in reverse direction
o/p is range [1-5] deleted
#sed -e '3,+5d' /etc/pwd - To delete from 3 & also continue to delete next 5 lines in file ,delete from specific line to END of file
o/p is range [3,...5 lines after this,4,5,6,7,8]
#sed -e '3,5!d' /etc/pwd - To delete everything except 3 to 5th line,NOT condition # delete except specific range lines
#Reverse of '3,5d'
# sed '1~3d' - To delete 1st lines,then delete 4th line 
# sed '2,4p' - To print lines b/w 2 to 4th line
#sed -n - To avoid repition
# sed -g - To replace all occurences
# NUMBER - To replace number match
# sed -p - print pattern match
# -i - ignore case
# ^ - Match empty string after new line
# $ - Match empty string before new line
# sed -m '/hello/$'
# sed -n '/hello/p' - print all matching lines 
###############
#REGEX 
#############
^ - starting of line
$ - ending of line
. - single character
* - one (or) more occurences
[chars] - Sequence of characters
###########
/a.c/ = Matches like "abc,a+c,a-c,a1c,catch,whereas pattern
/a*c/ = Matches like "adsasdsbc,a+c,a-c,a1c,catch,whereas pattern
/[tT]he/ = Matches the & The
/^$/ = empty lines
/ */ = Matches one (or) more spaces
[a-z] = single lowercase letter
[A-Z] = single uppercase letter
[0-9] = single number
[a-zA-Z0-9] = matches both number (or) letter
##############
Inbuilt CLASS functions 
[[:alnum:]] # [a-zA-z0-9]
[[:alpha:]]
[[:blank:]]
[[:cntrl:]]
[[:digit:]] # = [0-9]
[[:lower:]] # = [a-z]
[[:upper:]] # = [A-Z]
[[:space:]] # Whitespace
[[:punct:]]
[[:xdigit:]] # hex digits
[[:print:]]
[[:graph:]] # Any visible characters
##############
Multiple sed commands
sed -e '' -e '' -e '' file
#########
 cat res | sed -e 's/^[[:alnum:]]\{4\}/(&)-/g' i
# 's/^[[:alnum:]]//g' then print lines start with both char & numbers
# 's/^[[:alnum:]]{4}//g' then print 4 characters of lines start with both char & numbers,then change {4} to \{4\}
# 's/^[[:alnum:]]\{4\}/(&)/g' then (&) at the substitution side to add () for every first 4 charac like (line)
(line)-1first
(2323)-line2second
(line)-4foruth
(line)-5fifth
(line)-6sixth
(line)-7seventh
(line)-8eight
################

> cat y.txt | sed 's/\(.*\)\(.*-\)\(.*$\)/Area: \1 column: \2 value: \3/'
Area: (line)1 column: - value: first
Area: (line)4 column: - value: foruth
Area: (line)5 column: - value: fifth
Area: (line)6 column: - value: sixth
Area: (line)7 column: - value: seventh
Area: (line)8 column: - value: eight
############
> cat y.txt | sed 's/\(.*\)\(.*-\)\(.*$\)/Area: \1 column: \2 value: \3/'

############
#------Explanation below------
############
> cat y.txt | sed 's/(first pattern)(second pattern)(Third pattern $)/Area: {first pattern value } column: {second pattern value} value: {third pattern value}/'

> cat y.txt | sed 's/(.*)(.*-)(.*$)/<replace pattern>/'

> cat y.txt | sed 's/(.*)(.*-)(.*$)/  \1  \2   \3 /' # all 3 respective pattern values ( first/second/third)

> cat y.txt | sed 's/\(.*)\(.*-)\(.*$)/   \1  \2  \3/' # add "\" to avoid this escape charac

> cat y.txt | sed 's/\(.*\)\(.*-\)\(.*$\)/Area: \1 column: \2 value: \3/' # add the word u want to add "Area: Column: Value:"
