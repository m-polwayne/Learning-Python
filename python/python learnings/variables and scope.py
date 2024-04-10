def hh(*args,**kwargs):
    #print(args)
    j=kwargs
    j.update(hfh='k')

   # print(j)
    print(locals())

hh(1,2,3,4,5,6,how='fine',go='green')

def someFunc(func):
     print(func(5) + 2) 
someFunc(lambda x: x * 3)