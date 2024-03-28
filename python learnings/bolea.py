'''j=[7,8,9]
i=7
if i in j:
    print('true',j.index(i))

string='My name is Iron-Man,'
words=string.split(' ')

print(words)
print(string[0:7])
print(string[7:])
lists=[g for g in string.replace(' ','').replace(',','').replace('.','').lower()]
noM=[k for k in lists if k!='m']
sets=list(set(lists))

if 'n' in sets:
    print(len(sets))
print(sets)
print(noM)
print(lists)
l='*'.join(lists)
j=lists.copy()
print(j)
k=tuple(lists)
print(k[4])
print(k)
print(k.count('m'))
print(lists)
print(lists[:4])
'''
dict={'one':1,'two':2,'three':3,'four':4,}

