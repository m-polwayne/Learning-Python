# name=input(' enter name : ')
# surname=input(' enter surname : ')
# print("hello "+name.upper()+" "+surname.title())
# print("what do you calll a bear with no teeth?\n\nA gummy bear")
# print(len(name))


# num1=input(' enter first number : ')
# num2=input(' enter second number : ')
# if num1<num2:
#    print(num1+','+num2)
# else:
#    print(num2+','+num1)


# colours=input(' enter your favorite color : ')
# col=colours.lower()
# if col=='red':
#   print('I like red too')
# else:
#   print('I dont like '+col+", I like red")

# text = ' This is some text. '
# print(text.strip(' '))

from math import sqrt
import math
from operator import index
import random


# print(round(6.990707,2))
# print(sqrt(500))
# print(round(math.pi,5))
'''name=input('enter name: ')
num= int(input('enter a number: '))
if num >10:
    for i in range(0,3):   
        print('too high')
else:
    for i in range(0,num):   
        print(name)'''
'''fruit_tuple = ('apple','banana','strawberry','orange')
print(random.choice(fruit_tuple))'''

'''fruit_tuple = ('apple', 'banana', 'strawberry', 'orange')
for t in fruit_tuple:
    print(t)

pos = int(input("enter which pfruit index: "))
print(fruit_tuple[pos])
print(fruit_tuple.index(fruit_tuple[pos]))
l = ['f', 'g']
g = l.index('g')
del (l[g])
print(l)'''

'''
stri = 'MyNameIsMotshidisi'
stri = "".join([i if i.islower() else ' ' + i.lower()
               if i in ["I", 'N'] else " "+i for i in stri])
print(stri)


myTuple=('d', 'f', 'j')

myList=['a','a','b','c']

mySet={'a','b','c'}

myDictionary={'a':'d','b':'f','c':2}

filterdList=[item for item in myList if item%2==0]

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  
 
myDict = { k:v for (k,v) in zip(keys, values)}

myDict= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in myDict.items()}
print(double_dict1)'''
'''
subject=input(' enter your favourite subject: ')
for i in range(len(subject))[len(subject)::-1]: print(subject[i])'''
choice=int(input('''select an option 1,2 or 3
                 1) create a new file
                 2) display the file
                 3) add a new item tp the file 
                  make a selection: 1,2 or 3:
                 ''' ))
if choice !=1 and choice!=2 and choice!= 3:
    print("the choice you have entered does not exist") 
else:
    if choice ==1:
        subject=input('enter a school subject: ')
        f=open("Subject.txt",'w')
        f.write(subject+'\n')
        f.close()
    elif choice==2:
        f=open("Subject.txt",'r')
        print(f.read())
        f.close()
    else:
        subject=input('enter a new school subject: ')
        f=open("Subject.txt",'a')
        f.write(subject+'\n')
        f.close()
        f=open("Subject.txt",'r')
        print(f.read())
        
