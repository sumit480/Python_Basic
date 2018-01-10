#!/usr/bin/python

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self,x):
      self.x=x
      print("Calling parent constructor")
		

   def parentMethod(self):
      print('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr 

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self,y):
      #Parent.x=y #Accessing Base class member in derived class using base_class.member_name in D-class Constructor
      print("Calling child constructor",y)
	 

   def childMethod(self,z):
      Parent.x=z
      print('Calling child method',z)

# instance of child
c = Child(10)    
# child calls its method      
c.childMethod(20)
# calls parent's method
c.parentMethod() 
# again call parent's method    
c.setAttr(200)
# again call parent's method
c.getAttr()          