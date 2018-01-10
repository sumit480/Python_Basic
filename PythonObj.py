"""
class Student:
	#This is a python class and object example.
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	def disp(self):
		print("Name:",self.name,"Roll No.:",self.roll)
std1=Student("Rajesh",14)
std1.attr=16
std2=Student("Manish",23)

std2.attr=15

std1.disp()
std2.disp()
"""
class Complex:
	"""This is python class to print complex number"""
	def __init__(self,real=0,imag=0):
		self.real=real
		self.imag=imag
	def complexNum(self):
		print("{0}+{1}j".format(self.real,self.imag))
		
com1=Complex(4,6)
com2=Complex(7,5)

com1.complexNum()
com2.complexNum()