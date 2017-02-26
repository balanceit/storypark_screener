# main.py
from flatten import flatten

a = [[1,2,[3]],4]
b = [[[[0]]],1,2,[3,4,[5],6,[],[7,[8,[9],10]]],11,12,[[[[[[13]]]]]],[],14]

for i in [a,b]:
	print '\nbefore flattening:', i
	print ' after flattening:', flatten(i)