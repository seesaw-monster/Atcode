N = int(input())
t = N//5
A = t*5
B = (t+1)*5
if(abs(A-N)<abs(B-N)):
    print(A)
else:
    print(B)
