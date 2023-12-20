N,M=map(int,input().split())
C=input().split()
D=input().split()
P=list(map(int,input().split()))

# list.index(x[, start[, end]])
value=0
for i in range(N):
    try:
        value+=P[D.index(C[i])+1]
    except:
        value+=P[0]

print(value)

