

def my_var():
	a = 42
	b = "42"
	c = "quarante-deux"
	d = 42.0
	e = True
	f = [42]
	g = {42:42}
	h = (42,)
	i = set()
	print str(a) + " est de type < class 'int'>"
	print b + " est de type < class 'str'>" 
	print str(c) + " est de type < class 'str'>" 
	print str(d) + "  est de type < class 'float'>"
	print str(e) + "  est de type < class 'bool'>"
	print str(f) + "  est de type < class 'list'>"
	print str(g) + "  est de type < class 'dict'>"
	print str(h) + "  est de type < class 'tuple'>"
	print "set() est de type < class 'set'>"

if __name__ == '__main__':
	my_var()
