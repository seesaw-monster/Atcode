N = int(input())
A = input().split()
for i in range(len(A)):
    A[i]=int(A[i])
Q = int(input())
d_list = []

for _ in range(Q):
    l, r = map(int,input().split())
    s=0
    for i in range(1, N, 2):
        if r<A[i]:
            break

        if l>=A[i] and l<=A[i+1]:
            s+=A[i+1]-l
        elif l<A[i]:
            s+=A[i+1]-A[i]
        elif l>A[i+1]:
            s+=A[i+1]-A[i]
        elif r<A[i+1] and l>A[i]:
            s+=r-l
        elif r<A[i+1]:
            s+=r-A[i]

    print(s)
