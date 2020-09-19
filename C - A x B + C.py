def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return len(divisors)
n = int(input())
# A*B+C = N
counter = 0
for c in range(1, n-1//2):
    ans = n-c
    counter += make_divisors(ans)
print(counter)
