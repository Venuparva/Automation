import os
'''
  """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """ '''
output_list = dir_list = []
def find_path(path):
	files = os.listdir(path)
	for item in files:
		item = path+"/"+item #sChildPath = os.path.join(sPath,sChild)
                if os.path.isfile(item):
			output_list.append(item)
                else:
			dir_list.append(item)
find_path("/tmp")
print output_list
print "------"
print dir_list
print "****************"
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
#*********************
A0 = {'a':1,'b':2,'c':3,'d':4,'e':5}
A1 = [ 0,1,2,3,4,5,6,7,8,9]
A2 = [1,2,3,4,5] // becomes empty []
A3 = {'a':1,'b':2,'c':3,'d':4,'e':5}//[1,3,2,5,4]
A4 = [1,2,3,4,5]
A5 = [0,1,4,9,16,25] # {0:0,1;1,2:4,3:9...} 
A6 = [[0,0],[1,1],[2,4],[3,9],[4,16][5,25]...]
#==================
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 
print f(2) # 
f(3,[3,2,1])
f(3)
#============
class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A() 
b = B() 
c = C() 
d = D() 
e = E()

# specify output from here onwards

a.go() # go A go
b.go() # go A go,go B go
c.go() # go A go,go c go
d.go() # go B go,go A go,go D go//here D-->B-->A,similarly D-->C-->A hence A,C/B,D go will come
e.go()# go A go,go B go,go C go (or) Nothing//here E-->B-->A,similarly E-->C--->A so A,C,B 

a.stop() # stop A stop
b.stop() # stop A stop // printing from parent,since no stop() in local B
c.stop() # stop A stop & stop C stop # first parent then child
d.stop() # it will call super(D, self).stop() will call either stop A stop (or) error since self given ,but no self stop() given inside B, or it will inturn call stop() from A() # here D-->B(no stop function in it)-->A,similarly D--C-->A
in both case,it will end up in A,so answer is stop A stop,stop C stop,stop D stop ( A---C--D)
e.stop() # here E-->(C/B)--->A ,hence stop A stop ,stop C stop,since B & E don't have stop in it

a.pause() # Not implemented
b.pause() # nothing empty # here B-->A ,so Not implemented will print
c.pause() # nothing empty # here C--A, Not implemented
d.pause() # wait D wait
e.pause() # empty,no more pass functions in B & c,but either A() function pass will print? yes, E-->C/B-->A,hence A function code will print in it,o/p is Not implemented from A() will get print
#######################
######Tree object########
######################
class Node(object):
    def __init__(self,sName):
        self._lChildren = []
        self.sName = sName
    def __repr__(self):
        return "<Node '{}'>".format(self.sName)
    def append(self,*args,**kwargs):
        self._lChildren.append(*args,**kwargs)
    def print_all_1(self):
        print(self)
        for oChild in self._lChildren:
            oChild.print_all_1()
    def print_all_2(self):
        def gen(o):
            lAll = [o,]
            while lAll:
                oNext = lAll.pop(0)
                lAll.extend(oNext._lChildren)
                yield oNext
        for oNode in gen(self):
            print(oNode)

oRoot = Node("root")
oChild1 = Node("child1")
oChild2 = Node("child2")
oChild3 = Node("child3")
oChild4 = Node("child4")
oChild5 = Node("child5")
oChild6 = Node("child6")
oChild7 = Node("child7")
oChild8 = Node("child8")
oChild9 = Node("child9")
oChild10 = Node("child10")

oRoot.append(oChild1)
oRoot.append(oChild2)
oRoot.append(oChild3)
oChild1.append(oChild4)
oChild1.append(oChild5)
oChild2.append(oChild6)
oChild4.append(oChild7)
oChild3.append(oChild8)
oChild3.append(oChild9)
oChild6.append(oChild10)

# specify output from here onwards

oRoot.print_all_1()
oRoot.print_all_2()
