#functions are comprised of a name and parameters, and are denoted by the def statement
from math import prod


def performOperation(num1,num2,operation='sum',message='default message'):
    if operation =='sum':
        #print(num1+num2)
       return num1+num2
    if operation=='multiply':
        print( num1*num2)
    print(message)

def performOperations(*args,operations='sum'):
    if operations =='sum':
        print(sum(args))
    if operations=='multiply':
        print( prod(args))
    
 
print(performOperation(3,2,message='multiply',operation='sum'))
performOperations(1,3,5,7,7,9,operations='multiply')