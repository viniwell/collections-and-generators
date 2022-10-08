n=int(input('input amount-->'))
list=[int(s) for s in input('list-->').split()]
p=int(input('input number that should be added-->'))
list_2=[
    i
    for i in list
    if i!=p
]
list_2.insert(0,p)
print(' '.join([str(i) for i in list_2]))