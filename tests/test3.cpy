def factorial(x):
#{
## declarations ##
	#int i,fact

	fact = 1
	i = 1
	while i<=x:
	#{
		fact = fact * i
		i = i + 1
	#}
	print(fact)
	return fact
#}

def fibonacci(x):
#{
	if x<=1:
		return x
	else:
		return fibonacci(x-1)+fibonacci(x-2)
#}


#def main

	#int x,z

	x = int(input())
	z = int(input())

	print(factorial(x))
	print(fibonacci(z))