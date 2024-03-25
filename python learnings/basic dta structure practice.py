#LISTS
from operator import length_hint


myList =[1,1,2,3,4,4]
myList.append(5)
#print(myList)
b=myList.copy()
x=myList.pop()

print(myList)
print(x)
print(b)

print('##################################################')
###################################################################


#SETS sets are random not ordered and sets are immutable, 
#you cannot change a value in a set once declared but you 
#can add and remove elements from a set
d='jjvbdygdudhghcx'
mySet={"a",'b','c'}
mySet.update('646')
print(mySet)
newSet=list(set(myList))#sets contain unique(no repetition)
print("myList = " ,myList)
print("set made from myList = " ,newSet)
print(len(myList))
print("d as a list",list(d))
print("d as a set",set(d))
j= list(d)

v= set(d)
v.discard('j')
print(v)
print(len(d))
print(len(j))
print(len(v)) 
print('##################################################')
#################################################################

#TUPLES tuples are like lists but they are immutable and declared 
#using tuple= ('t','u','p','l','e') and list = ['l','i','s','t']
myTuple=('d', 'f', 'j')
type(myTuple)
u=myTuple[2]
k='j'
h='h'
if 'd'not in myTuple:
    print('yes')
else: 
    print('no')
print(myTuple)
print(type(myTuple))
print('##################################################')
#################################################################
#DICTIONARIES dictionaries have key value pairs like a dictionary
dictionary={"0":0, "1":1, "2":2, "3":3, "4":4,}

thisdict = dict(name = "John", age = 36, country = "Norway")
print('original dictionary ', thisdict) 
thisdict.update(name='Motshidisi')#adding to a dict using update
print('dictionary after name update thisdict.update(name=Motshidisi)',thisdict) 
thisdict['age']=26 #update using subscript
print('dictionary after age update #thisdict[age]=26',thisdict) 
#adding new key value pair to dictionary using update method
thisdict.update({'surname':'Pholoane'})
f1=dict(country ="south ahhh", province=' limpompo',)
thisdict.update(f1)

print('dictionary after adding new key value pair surname',thisdict) 
print(thisdict.get('name'))
thisdict
print('##################################################')
#################################################################
#LIST COMPREHENSIONS
m=[2*item for item in myList]
print(m)
print(myList)
filterdList=[item for item in myList if item%2==0]
print(filterdList)
myString='today is day 2 of studying python. tommorow will be day 3'
splitString =myString.split()
print(splitString)

def cleanString(tring):
    return tring.replace('.','').lower()

yes=[cleanString(ring) for ring in splitString]
print(yes)
filterYes=[cleanString(ring) for ring in splitString if type(cleanString(ring))]
print(filterYes)