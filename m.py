a=[]

key=0
while key==0:
    n=input().split()
    if n[0]=='push_back':
        a.append(n[1])
        print('ok')
    
    elif n[0]=='push_front':
        a.insert(0,n[1])
        print('ok')
    
    elif n[0]=='pop_back':
        print(a[-1])
        a.pop(-1)
    
    elif n[0]=='pop_front':
        print(a[0])
        a.pop(0)
    
    elif n[0]=='front':
        print(a[0])
    
    elif n[0]=='size':
        print(len(a))
    
    elif n[0]=='clear':
        a.clear()
        print('ok')
    
    elif n[0]=='exit':
        print('bye')
        key=1