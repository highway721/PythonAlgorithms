N, K, M = map(int, input().split())
score = sum(map(int, input().split()))


if score>=N*M:
    print(0)
elif (N*M)-score>K:
    print(-1)
elif (N*M)-score<=K:
    print((N*M)-score)