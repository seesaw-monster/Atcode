# import sys
# sys.setrecursionlimit(10**6)
A, B, C = map(int, input().split())

if A==B==C:
    print('Yes')
elif A==B+C or B==A+C or C==A+B:
    print('Yes')
else:
    print('No')

