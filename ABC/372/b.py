M = int(input())

a_max = 10

A = []
for a in range(a_max+1)[::-1]:
    if M >= 3**a:
        c = M//3**a
        M-=c*3**a
        for _ in range(c):
            A.append(a)

print(len(A))
print(*A[::-1])
