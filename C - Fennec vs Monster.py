H, N = map(int, input().split())
A = [int(x) for x in input().split()]
list2 = sorted(A, reverse=True)  # reverseをTrueに

if N>H:
    print(0)
elif N>0:
    del list2[0:N]
    print(sum(list2))
elif N<=0:
    print(sum(A))
