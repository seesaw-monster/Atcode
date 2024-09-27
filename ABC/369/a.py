A, B = map(int, input().split())

if A == B:
    print(1)
    exit()
elif B < A:
    tmp = A
    A = B
    B = tmp

if (B-A)%2 == 0:
    print(3)
else:
    print(2)
