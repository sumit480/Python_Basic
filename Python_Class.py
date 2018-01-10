#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)
   def __del__(self):
	class_name=self.__class__.__name__
	print(class_name,"Destroyed")
		

'This would create first object of Employee class'
emp1 = Employee("Zara", 2000)
'This would create second object of Employee class'
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" %Employee.empCount)

"""Using Built-in function to access and manipulate the object attributes"""
#Getting the attribute value.
print(getattr(emp2,'salary'))

#setting a new attribute
setattr(emp1,'age',28)
setattr(emp2,'age',30)
print(getattr(emp1,'age'))
#Check if the Object has attribute: return True/False
print(hasattr(emp1,'id'))
delattr(emp1,'age')
print(hasattr(emp1,'age'))
#Class attributes available in Python
print("The Class dictionary is: ",Employee.__dict__)
print("The docs for this class: ",Employee.__doc__)
print("Modules: ",Employee.__module__)
print("Class Name: ",Employee.__name__)
print("Bases: ",Employee.__bases__)