a=[]

key=0
while key==0:
    n=input().split()
    if n[0]=='push':
        a.append(n[1])
        print('ok')
    elif n[0]=='pop':
        print(a[len(a)-1])
        a.pop(int(a[len(a)-1]))
    elif n[0]=='back':
        print(a[len(a)-1])
    elif n[0]=='size':
        print(len(a))
    elif n[0]=='clear':
        a.clear()
        print('ok')
    elif n[0]=='exit':
        print('bye')
        key=1
