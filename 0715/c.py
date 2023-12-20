N=int(input())
s=[]
c=[False]*N
cN=N
for i in range(N):
    s.append(input())
 
for i in range(N):
    if c[i]:
        continue
 
    for j in range(i+1,N):
        if c[j]:
            continue
 
        if s[i]!=s[j] and s[i]!=s[j][::-1]:
            continue
        else:
            c[j]=True
            cN-=1
 
print(cN)
