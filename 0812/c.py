N,M=map(int,input().split())
S=list(input())


C=list(map(int,input().split()))

color=set()
for c in C:
    color.add(c)

for c in color:
    before_s=''
    first_n=2*10**5+1
    for n in range(N):
        if C[n]==c and before_s=='':
            before_s=S[n]
            first_n=n
        elif C[n]==c:
            tmp=S[n]
            S[n]=before_s
            before_s=tmp
    if first_n!=2*10**5+1:
        S[first_n]=before_s


return_s=''
for s in S:
    return_s+=s
print(return_s)
