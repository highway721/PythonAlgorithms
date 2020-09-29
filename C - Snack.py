a,b=sorted(map(int,input().split()))

# 最大公約数
def gcd(a, b):
  if b==0:
     return a
  else:
     r = a%b
     return gcd(b,r)

# print(int(a*b/gcd(a,b)))
print(gcd(a,b))
