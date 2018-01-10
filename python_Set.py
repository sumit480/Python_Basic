"""Python Set is a heterogenious collection, It restricts duplicacy of elements,
Always contains data in sorted,no matter how you define your set.
Defined as enclosed within curly braces, seperated by comma.
Properties of set in python:
--> It support Union, Intersection, difference, Subset, add, remove, pop operations.
"""

mySet1={"Rohan",1,False,4.5,8}
print("Set 1 contains: ",mySet1)

mySet2={"Rajesh",78,9.0,12.234,1,True}
print("Set 2 contains: ",mySet2)

##Union of two sets: It returns a new set so we will store this in third set.

mySet3=mySet1.union(mySet2)
print("After union of set1 and set2: ",mySet3)

##Intersection of two sets:
mySet4=mySet1.intersection(mySet2)
print("After Intersection of set1 and set2: ",mySet4)

##difference of set1 and set2:
mySet5=mySet1.difference(mySet2)
print("The difference of Two sets are",mySet5)

##adding elements:
mySet1.add(5)
print("After adding 5: ",mySet1)

##Removing an element:
mySet1.remove(4.5)
print("After removal: ", mySet1)

##pop element: Pop will delete the very first element in the set
mySet2.pop()
print("After Pop: ",mySet2)

##Clear will remove all the elements from the set:
mySet5.clear()
print("After clear: ",mySet5)