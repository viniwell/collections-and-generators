n=int(input('input amount-->'))
list=[int(s) for s in input('list').split()]
p=int(input('input number that should be deleted-->'))
print(' '.join([str(i) for i in list if i!=p]))