import threading
import time
from unittest import result

def longSquare(num,results):
    time.sleep(1)
    results[num]= num**2
#[longSquare(n) for n in range(1,5)]
results={}

t1= threading.Thread(target=longSquare,args=(1,results))
t2= threading.Thread(target=longSquare,args=(2,results))
t3= threading.Thread(target=longSquare,args=(3,results))
t3.start()
t1.start()
t2.start()
#t3.start()

t3.join()
t1.join()
t2.join()


print (results)