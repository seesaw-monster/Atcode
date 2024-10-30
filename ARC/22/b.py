# import sys
# sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int, input().split()))

r = 0
cm = 0
s = set()

# s.add(A[0])

for l in range(N):
    while r < N and (len(s)==0 or not A[r] in s):
        s.add(A[r])
        r+=1

    if cm < len(s):
        cm = len(s)
    s.remove(A[l])

print(cm)
