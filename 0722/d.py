N,M=map(int,input().split())
S=[]
# C=[]

for _ in range(N):
    S.append(input())
    # C.append([0]*M)

def move(i,j,c,start_i,start_j):
    if i==start_i and j==start_j and c>0:
        return c

    if S[i][j]=='.':
        c+=1

    c_list=[0]*5
    c_list[0]=c

    if i<N-1:
        c_list[1]=move(i+1,j,c,start_i,start_j)
    if j<M-1:
        c_list[2]=move(i,j+1,c,start_i,start_j)
    if i>1:
        c_list[3]=move(i-1,j,c,start_i,start_j)
    if j>1:
        c_list[4]=move(i,j-1,c,start_i,start_j)

    return max(c_list)

print(move(1,1,0,1,1))
