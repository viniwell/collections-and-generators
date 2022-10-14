n=int(input())
a=input().split()
m=int(input())
b=input().split()
ans=[int(x) for x in a]
for i in range(m+1):
    if i>n:
        ans.append(0)
    ans[i]+=int(b[i])
answ=' '.join(str(x) for x in ans)
print(answ)