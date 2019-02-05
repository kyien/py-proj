#varible scope in functions
a=5 #global scope

def number_print(num):
	global a
	a=num
	#return b
	

number_print(90)
print(a)
