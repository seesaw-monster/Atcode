N=int(input())
A=list(map(int,input().split()))

c=0
while max(A)-min(A)>1:
    # A=sorted(A)
    min_index=min(range(len(A)), key=A.__getitem__)
    max_index=max(range(len(A)), key=A.__getitem__)
    diff=A[max_index]-A[min_index]
    d=len(str(diff))-1
    if diff<=2*10**d:
        d=max(0,d-1)
    # d=max(0,d)
    A[min_index]+=10**d
    A[max_index]-=10**d
    c+=10**d

print(c)
