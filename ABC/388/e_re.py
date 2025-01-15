from collections import deque
N = int(input())
A = list(map(int, input().split()))

"""
解1
l = 0
r = N//2+1

max_k = 0

while l<r:
    K = (l+r)//2

    can_make = True
    for k in range(K):
        if A[k]*2<=A[N-K+k]:
            continue
        else:
            can_make = False
            break

    if can_make:
        if max_k<K:
            max_k = K
        l = K+1
    else:
        r = K

print(max_k)
"""

# 解2
max_k = 0

left = deque(A[:N//2][::-1])
right = deque(A[N//2:][::-1])
r = None

while len(left) and len(right):
    l = left.popleft()
    r = right.popleft() if r==None else r

    if l*2<=r:
        r = None
        max_k+=1

print(max_k)
