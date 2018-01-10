##Python List Example
"""This Code will tell about basic implementation of List in
and it Operation including methods available for list"""

myList=[1,4,'amit',465,"Rajesh",True]
print(myList)

#Append at last
myList.append(False)
print("After append",myList)

#Insert Operation
myList.insert(2,'sunil')
print("After Insert: ",myList)

##Pop Operation
print("Deleting last Value",myList.pop())
print("Deleting Specified index 1 value: ",myList.pop(1))
print(myList)

myList2=[1,5,2,3,90,7,78,45,32,12]

#Sorting a list
"""Caution: Sorting will be done for homogeneous elements in the List only"""
myList2.sort()
print("Sorted List:",myList2)

#Deletion of element
del myList[3]
print("After deletion",myList)

#getting an index of List element
print("The index of 78 is:",myList2.index(78))

#removing an element
print("Removing 78 from the List",myList2.remove(78),myList2)
print("Counting the number of occurences of 2:",myList2.count(2))