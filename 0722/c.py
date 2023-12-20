N=int(input())
A=list(map(int,input().split()))

for n in range(N):
    # 回数カウント
    c_list=[0]*N
    c_list[n]+=1

    # 組み合わせ記録
    b=[n+1]
    b.append(A[n])

    # 閉じているかどうか
    close=False

    # 次のn
    next_n=n
    while True:
        # 次の移動さき
        next_n=A[next_n]-1
        c_list[next_n]+=1
        b.append(A[next_n])

        if c_list[n]==2:
            close=True
            break
        elif max(c_list)==2:
            break

    if close and len(b[:-1])>=2:
        print(len(b[:-2]))
        print(*b[:-2])
        break
