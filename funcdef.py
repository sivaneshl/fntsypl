# function defn

def fibo(n): # this function will return  fibonacci series upto n
	result = []
	a, b = 0, 1
	while a < n:
		#result = result + [a]
		result.append(a)
		a, b = b, a+b
	return result

f100 = fibo(1000)
print f100	

	