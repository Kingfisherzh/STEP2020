def foo(b):
	#print('id(b): %#08x' % id(b))
	b.append(2)
	print('id(b0): %#08x' % id(b[0]))
	print('id(b1): %#08x' % id(b[1]))
	b = b + [3]
	b.append(4)
	print('b:', b)
	print('id(b): %#08x' % id(b))
	print('id(b0): %#08x' % id(b[0]))
	print('id(b1): %#08x' % id(b[1]))
	print('id(b2): %#08x' % id(b[2]))
	print('id(b3): %#08x' % id(b[3]))
	
a = [1]
foo(a)
print('a:', a)
print('id(a): %#08x' % id(a))
print('id(a0): %#08x' % id(a[0]))
print('id(a1): %#08x' % id(a[1]))
