n=int(input('input amount-->'))
dict=dict(math=0,
phisics=0,
python=0)

for i in range (n):
    list=[str(s) for s in input('list with marks-->').split()]
    marks_count=3
    for i in range(len(list)):
        if i>0:
            if i==1:
                list[i]=int(list[i])
                dict['math']+=list[i]
            elif i==2:
                list[i]=int(list[i])
                dict['phisics']+=list[i]  
            elif i==3:
                list[i]=int(list[i])
                dict['python']+=list[i]               
for i in dict.keys():
    dict[i]=(f'{(dict[i]/3):.2f}')
print('-'*30)
print(dict['math'], dict['phisics'],dict['python'])