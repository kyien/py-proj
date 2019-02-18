# A prime number is only divisible by 1 and itself
def prime_check(num):
	if num <=0:
		print('Not applicable')
	elif num==1:
		print('number is not prime ')
	else:
		for k in range(2,num):
			if (num%k)==0:
				print(num,'is not a prime number')
				break
			
			else:
				print(num,'is a prime number')

print('*****PRIME NUMBER CHECK*****')
num=int(input('Enter the number to check :'))
prime_check(num)
	

				

	
         
