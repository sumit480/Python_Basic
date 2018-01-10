class Parent:
    def myMethod(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
        #print(self.c)
    def getValue(self):
        return self.c
class Child(Parent):
    def getValue(self):
        print(self.c) #Overriding the methods in parent class
c=Child()
c.myMethod(10,20)
c.getValue()
