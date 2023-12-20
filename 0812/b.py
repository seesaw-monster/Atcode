N=int(input())

C=[]
A=[]
for _ in range(N):
    C.append(int(input()))
    A.append(list(map(int, input().split())))

X=int(input())
K=0
B=[]
min_c=38

for i in range(N):
    for j in range(C[i]):
        if A[i][j]==X and min_c>C[i]:
            K=1
            B=[i+1]
            min_c=C[i]
            break
        elif A[i][j]==X and min_c==C[i]:
            K+=1
            B.append(i+1)
            break

print(K)
print(*B)
