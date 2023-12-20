N=int(input())
P=list(map(int,input().split()))
P1 = P[0]
P=sorted(P, reverse=True)

x=P[0]-P1+1
if len(P)>1:
    if P[0]==P1 and P[0]!=P[1]:
        x=0
else:
    x=0

print(x)
