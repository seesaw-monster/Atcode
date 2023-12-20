H_a, W_a=map(int,input().split())
A=[]
for _ in range(H_a):
    A.append(input())

H_b, W_b=map(int,input().split())
B=[]
for _ in range(H_b):
    B.append(input())

H_x, W_x=map(int,input().split())
X=[]
for _ in range(H_x):
    X.append(input())

H_c=20
W_c=20
C=[]
AB=[]
for _ in range(H_c):
    C.append('.'*W_c)
    AB.append([])

for i in range(H_c):
    for j in range(W_c):
        AB[i].append('C')

