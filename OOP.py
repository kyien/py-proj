#Objects in python

class calc:
	#age=5
	def __init__(self,age,name):
		self.age=age
		self.name=name
	

	def num_comparison(self):
		print(self.age)
		print(self.prime_no_check())


	def prime_no_check(self):
		print('dest!')

	#def to_text_file(self):

class comp(calc): #inheritance
	def struct():
		print('Horray')


cl=calc(35,'Nathan') #instantiation
cl.num_comparison() #access class methods and properties using the dot accessor.
