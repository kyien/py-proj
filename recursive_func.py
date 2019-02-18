#Recursion in functions
#factorial

def factorial(num):
	if num<=0:
		num=None
		return num
	elif num==1:
		return num
	else:
		return num*factorial(num-1)

print('******FACTORIAL COMPUTATION******')
num=int(input('Enter number :'))
print('The factorial of ',num,' is ',factorial(num))
