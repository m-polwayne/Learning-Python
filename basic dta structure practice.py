#LISTS
from operator import length_hint


myList =[1,1,2,3,4,4]
myList.append(5)
#print(myList)
b=myList.copy()
x=myList.pop()

#print(myList)
#print(x)
#print(b)


##################################################

#TUPLES AND SETS
d='jjvbdygdudhghcx'
mySet={"a",'b','c'}
print(mySet)
newSet=list(set(myList))#sets contain unique(no repetition)
print("myList = " ,myList)
print("set made from myList = " ,newSet)
print(len(myList))
print("d as a list",list(d))
print("d as a set",set(d))