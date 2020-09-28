N=int(input())
a = [int(x) for x in input().split()]
count=1
mini=a[0]

for i in range (1,N):
    if a[i]<mini:
        count=count+1
        mini=a[i]

print(count)





