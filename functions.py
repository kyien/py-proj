#functions in python
def print_str(str):
	print(str)

text='I am strong'
#print_str(text)

def num_check(num1,num2):
	res=0
	if num1>num2:
		res=num1
	else:
		res=num2
	return res
print('*******PROGRAM TO COMPARE NUMBERS ')
x=int(input('enter the first number'))
y=int(input('enter the second number'))
print('the comparison between num1 & num 2 ...',num_check(x,y))


