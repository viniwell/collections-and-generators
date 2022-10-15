a=[]
n=input().split()
while n[0]!='exit':
    if n[0]=='push':
        a.append(n[1])
    elif n[0]=='pop':
        print(a[len(a)-1])
        a.pop(a[len(a)-1])
    elif n[0]=='back':
        a.pop(a[len(a)-1])
    elif n[0]=='size':
        print(len(a))
    elif n[0]
