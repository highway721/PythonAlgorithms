A, B, K = map(int, input().split())

if A>=K:
    A=A-K
    B=B
    print(A,B)
elif A<K and K-A<B:
    print(0,B-(K-A))

elif A<K and K-A>B:
    print(0,0)
else:
    print(0,0)