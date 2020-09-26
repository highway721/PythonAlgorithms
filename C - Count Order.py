import itertools
N=int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
PP=tuple(P)
A=list(itertools.permutations(range(1,N+1)))
PW=(A.index(P))
QW=(A.index(Q))
print(abs(PW-QW))


