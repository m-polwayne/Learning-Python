for i in range(1,101):
    if i%15==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)
i=0
while i<20:
    print("I am a winner",i)
    i+=1
t=[i for i in range(101)[::-5]]
print(t)
func=lambda x:x*x
def get():
    print(func(5)*4)
get()