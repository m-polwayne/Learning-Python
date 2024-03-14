

def diamond(num):
    for i in range(1,num+1):
        i=i-(num//2 +1)
        if i<0:
            i=-i
        print(" "*i+"*"*(num-2*i)+" "*i)

diamond(13)