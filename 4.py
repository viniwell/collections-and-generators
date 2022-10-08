n=int(input('input amount-->'))
dict={}
magazine=[]
for i in range (n):
    list=[str(s) for s in input('list with marks-->').split()]
    magazine.append(list[0])
    marks_count=len(list)-1
    for i in range(len(list)):
        if i>0:
            list[i]=int(list[i])
    dict[list[0]]=list[1:]
for i in dict.keys():
    dict[i]=(f'{((sum(x for x in dict[i]))/marks_count):.2f}')
for i in magazine:
    print(i, dict[i])
