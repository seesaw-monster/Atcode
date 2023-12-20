from decimal import Decimal
N=int(input())

def clear(a,b):
    return a/(a+b)

AB=[]
for i in range(N):
    ai,bi=map(Decimal,input().split())
    AB.append([ai,bi,i+1])

AB.sort(key=lambda x: x[0]/(x[0]+x[1]),reverse=True)

ans=[x[2] for x in AB]
print(*ans)
