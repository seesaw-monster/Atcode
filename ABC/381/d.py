# import sys
# sys.setrecursionlimit(10**6)
from collections import deque
N = int(input())
A = list(map(int, input().split()))

max_n = 0
s = set()
q = deque()

for i in range(0, N-1, 2):
    if A[i]==A[i+1]:
        if not A[i] in s:
            s.add(A[i])
            q.append(A[i])
        else:
            if max_n<2*len(s):
                max_n = 2*len(s)

            x = q.popleft()
            s.remove(x)
            while x!=A[i]:
                x = q.popleft()
                s.remove(x)

            s.add(A[i])
            q.append(A[i])

    else:
        if max_n<2*len(s):
            max_n = 2*len(s)

        s = set()
        q = deque()

if max_n<2*len(s):
    max_n = 2*len(s)
            
s = set()
q = deque()

for i in range(1, N-1, 2):
    if A[i]==A[i+1]:
        if not A[i] in s:
            s.add(A[i])
            q.append(A[i])
        else:
            if max_n<2*len(s):
                max_n = 2*len(s)
            x = q.popleft()
            s.remove(x)
            while x!=A[i]:
                x = q.popleft()
                s.remove(x)
            s.add(A[i])
            q.append(A[i])
    else:
        if max_n<2*len(s):
            max_n = 2*len(s)

        q = deque()
        s = set()

if max_n<2*len(s):
    max_n = 2*len(s)

print(max_n)
