#c='hello world';
#print(c*2);
#print(c[0:6]);


def factorial(n):
    f=n;
    if type(n)!= int:
        print('n is not an interger');
    elif n<0:
        print('n cannot be a negative number'); 
    elif type(n)==float :
        print('n must be an interger');
    else:
        while n > 1:
            f=f*(n-1);
            n=n-1;
        print(f);

factorial(9)