N = int(input())
A = list(map(int, input().split()))

def f(x):
    count = 0

    while x%2==0:
        count+=1
        x//=2

    return count

A = sorted(list(map(f, A)))
print(A[0])
