N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
count = 0
while True:
    count+=1
    A[0]-=1
    A[1]-=1
    A.sort(reverse=True)

    if A[0] == 0 or A[1] == 0:
        break

print(count)
