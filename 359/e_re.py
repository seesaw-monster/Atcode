N = int(input())
H = list(map(int, input().split()))

cost = []

for i in range(N):
    if i == 0:
        cost.append(H[i]+1)
        continue

    for j in range(i)[::-1]:
        if H[j] < H[i]:
            H[j] = H[i]
        else:
            break

    cost.append(sum(H[:i+1])+1)

print(*cost)
