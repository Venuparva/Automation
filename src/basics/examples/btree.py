Plist = []
class Tree(object):
	def __init__(self,val):
		self.node = val
	def append(self,*args,**kwargs):
		Plist.append(*args,**kwargs)
 	def print_Tree(self,*args,**kwargs):
		print(self.node)
		for item in Plist:
		       print "Node {}".format(item.node)
#Create objects with respective node name string inside it,append all inside root-->1-->2-->3
#under 3-->4-->5-->6.....etc
root = Tree("root")
child1 = Tree("child1")
child2 = Tree("child2")
child3 = Tree("child3")
child4 = Tree("child4")
child5 = Tree("child5")
child6 = Tree("child6")
child7 = Tree("child7")
child8 = Tree("child8")
child9 = Tree("child9")
child10 = Tree("child10")
child11 = Tree("child11")
root.append(child1)
root.append(child2)
root.append(child3)
child1.append(child4)
child1.append(child5)
child2.append(child6)
child2.append(child7)
child3.append(child8)
child3.append(child9)
child6.append(child10)
child6.append(child11)
root.print_Tree(root)
