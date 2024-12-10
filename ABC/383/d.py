# import sys
# sys.setrecursionlimit(10**6)
N = int(input())

answer = 0
for i in range(int(N**(1/2))+1):
    c = 0
    for j in range(2, i):
        if i**2 % j == 0:
            c+=1

        if c > 3:
            break

    if c==3:
        print(i**2)
        answer+=1

print(answer)
