import os
import sys
print sys.argv[0]
print sys.argv[1]
print sys.argv[2]
'''
#o/p below 
Venu:python_tips venu$ python argnew.py hello
argnew.py
Venu:python_tips venu$ python argnew.py hello
argnew.py
hello
Venu:python_tips venu$ python argnew.py -c pwd
argnew.py
-c
Venu:python_tips venu$ python argnew.py -m
argnew.py
-m
Venu:python_tips venu$ python argnew.py -c pwd
argnew.py
-c
pwd
Venu:python_tips venu$
'''
# -*- coding: iso-8859-15 -*-

currency = u"€"
print ord(currency)

#UTF-8 - either through the signature or an encoding declaration 
