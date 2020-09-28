N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
#トータルポイント
total=sum(B)
ans=0
#ボーナス
for j in range(len(A)-1):
    if(A[j]-A[j-1]==1):
        ans=ans+C[j-1]

print(total+ans)


