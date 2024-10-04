# import sys
# sys.setrecursionlimit(10**6)
n, X = map(int, input().split())
A = list(map(int, input().split()))

b = list(bin(X)[2:])[::-1]

price = 0

for i in range(len(b)):
    if b[i]=='1':
        price += A[i]

print(price)
