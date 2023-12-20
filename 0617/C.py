import numpy as np
N=int(input())
A=list(map(int,input().split()))
B=np.zeros(3*N+1)

s=''
for i in range(3*N):
    B[A[i]]+=1
    if(B[A[i]]==2):
        s+=f'{A[i] } '
        
print(s[:-1])
