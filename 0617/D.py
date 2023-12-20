N=int(input())
XY=[]
ss = 0
for j in range(N):
    if ss>1:
        XY.append(list(map(int,input()[:-(ss-1)].split())))
    else:
        XY.append(list(map(int,input().split())))

    if j == 0:
        v = XY[j][1]
        while v>int('1'+'0'*ss):
            ss+=1
        if ss>1:
            XY[j][1]=int(str(XY[j][1])[:-(ss-1)])


s=0
i=0
while True:
    # print(i)
    if XY[i][0]==1:
        max_i=i
        max_Y=XY[i][1]
        i+=1
        while XY[i][0]==1:
            if XY[i][1]>max_Y:
                max_i=i
                max_Y=XY[i][1]
            i+=1
            if i==N:
                break
        if i==N:
            if max_Y>=0:
                s+=max_Y
            break
        # マイナスについても考える
        max_2i=i
        max_2Y=XY[i][1]
        i+=1
        while XY[i][0]==0:
            if XY[i][1]>max_2Y:
                max_2i=i
                max_2Y=XY[i][1]
            i+=1
            if i==N:
                break

        if (max_Y+max_2Y)>=0:
            s+=max_Y+max_2Y
    else:
        if XY[i][1]<=0 and i!=(N-1) and XY[i+1][0]!=0:
            t=i
            i+=1
            max_Y=0
            while XY[i][0]==1:
                if max_Y<XY[i][1]:
                    max_Y=XY[i][1]
                i+=1
                if i==N:
                    break
            if (max_Y+XY[t][1])>=0:
                s+=(max_Y+XY[t][1])
        elif XY[i][1]<=0:
            i+=1
        else:
            s+=XY[i][1]
            i+=1
    if i==N:
        break

if ss>1:
    print(str(s)+'0'*ss)
else:
    print(s)
