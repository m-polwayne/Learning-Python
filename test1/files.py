import csv


with open('me.csv','w') as j:
    j.writelines('name,surname,age,occupation \n',)
    j.writelines('Motshidisi,Pholoane,26,intern cyber security \n')
    j.writelines('Motshidisi,Pholoane,26,intern cyber security')
with open('me.csv','r') as f:
    i=csv.DictReader(f,delimiter=',')
    #next(i)
    for row in i:
        print(row)