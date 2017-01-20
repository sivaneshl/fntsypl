# filter 

def factor5(x):
	return x % 5 == 0
print filter (factor5, range(100))

# map
def cube(x):
	return x*x*x
print map (cube, range(1,11))	

# Reduce
def fnsum(x,y):
	return x + y
print reduce(fnsum, range(1,11))	