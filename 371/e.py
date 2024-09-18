N = int(input())
A = list(map(int, input().split()))
B = [{}, set([A[0]])]

# for i in range(1, N):
#     B.append(B[-1] | set({A[i]}))

f = 0
for i in range(N):
    for j in range(N):
        f+=len(set(A[i:j+1]))

print(f)

