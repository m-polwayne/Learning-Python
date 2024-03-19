f= open('countries.txt','a')
name =input('enter a name:')
f.write(name+'\n')
f.close()

f= open('countries.txt','r')
print(f.read())

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
        
