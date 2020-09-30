import math

x=int(input())
def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

while prime(x) == False:
    x += 1
print(x)