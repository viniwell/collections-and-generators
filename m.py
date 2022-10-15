a=[]

key=0
while key==0:
    n=input().split().strip()
    if n[0]=='push_back':
        a.append(n[1])
        print('ok')
    
    elif n[0]=='push_front':
        a.insert(0,n[1])
        print('ok')
    
    elif n[0]=='pop_back':
        if len(a)>0:
            print(a.pop(0))
        else: print('error')
    
    elif n[0]=='pop_front':
        if len(a)>0:
            print(a.pop(0))
        else: print('error')
    
    elif n[0]=='front':
        if len(a)>0:
            print(a[0])
        else: print('error')
    
    elif n[0]=='size':
        print(len(a))
    
    elif n[0]=='clear':
        a.clear()
        print('ok')
    
    elif n[0]=='exit':
        print('bye')
        key=1