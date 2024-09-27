N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)

Alice = 0
Bob = 0

for i in range(len(a)):
    if i%2==0:
        Alice+=a[i]
    else:
        Bob+=a[i]

print(Alice-Bob)
