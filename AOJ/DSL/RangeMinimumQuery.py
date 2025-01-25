n, q = map(int, input().split())
N = 2
while N<n:
    N*=2
A = [2**31 - 1 for _ in range(2*N)]

def find(s, t):
    # minimum element in a_s, ..., a_t
    left = (s-1)+N
    right = (t-1)+N

    min_left = A[left]
    min_right = A[right]

    while left//2!=right//2:
        if left%2==0 and left+1<right:
            min_left = min(min_left, A[left+1])
        left//=2

        if right%2==1 and right-1>left:
            min_right = min(min_right, A[right-1])
        right//=2

    return min(min_left, min_right)

def update(i, x):
    # change a_i to x
    I = N+i
    A[I]=x

    while I>1:
        if I%2==0:
            A[I//2]=min(A[I], A[I+1])
        else:
            A[I//2]=min(A[I-1], A[I])
        I//=2

for _ in range(q):
    com, x, y = map(int, input().split())

    if com==0:
        update(x, y)
    else:
        print(find(x+1, y+1))
        # print(A)
