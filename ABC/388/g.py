from collections import deque
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())
    L-=1
    R-=1
    diff = R-L
    max_k = 0
    left = deque(A[L:R-diff//2][::-1])
    right = deque(A[R-diff//2:R+1][::-1])
    # print(L+1, R+1)
    # print(left)
    # print(right)

    r = None
    while len(left) and len(right):
        l = left.popleft()
        r = right.popleft() if r == None else r

        if l*2<=r:
            r = None
            max_k+=1

    print(max_k)

