f= open('countries.txt','w')
f.write('south Ahhhh\n')
ans=1
while ans==1:
    num1=int(input('enter an interger: '))
    num2=int(input('enter another interger: '))
    sum=num1+num2
    f.write(str(num1)+" + " + str(num2) + " = "+str(sum)+'\n')
    ans=int(input('do you want to continue adding, yes=1 no=0: '))

f.close()
f= open('countries.txt','r')