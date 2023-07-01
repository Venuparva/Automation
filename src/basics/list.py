Z = [ ('A','b'),('B','c'),('C','a')]
H = []
S = []
res = []
for item in Z:
	for val in item:
		print val
		if val.islower() and val not in S:
			print "true"
			S.append(val)
		elif val not in H:
			print "false"
			H.append(val)
		print "-----"
print H
print S
print [(x,y) for x in H for y in S if x == y.upper()]
o/p is [('A', 'a'), ('B', 'b'), ('C', 'c')]
