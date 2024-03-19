f= open('countries.txt','a')
name =input('enter a name:')
f.write(name+'\n')
f.close()

f= open('countries.txt','r')
print(f.read())
