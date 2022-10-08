n=int(input('input amount-->'))
list=[int(s) for s in input('list-->').split()]
p=int(input('input number that should be deleted-->'))
q, k=map(int, [int(s) for s in input().split(' ')])

list.pop(p-1)
list.insert(q-1, k)

print(' '.join([str(i) for i in list]))