#control/Decision Making statements

#if statement
#if..else statements
#nested if statements
#elif statement
print('*******Starting a transaction*****')
amount=int(input("Enter amount to withdraw: "))
discount=0

if amount <1000: 
	discount=amount *0.45
	print('Net amount is: ', amount+discount)
elif amount <2000:
	discount=amount*0.5
	print('Net amount is: ', amount+discount)
else:
	discount=amount *0.7
	print( 'Net amount is : ',amount+discount)

#print('Net amount :',amount+discount)

