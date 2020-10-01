n, m = list(map(int, input().split()))

ac = [0] * (n+1)
wa = [0] * (n+1)
pena = 0

for i in range(m):
    question, answer = input().split()
    question = int(question)
    if (answer == "AC") and (ac[question] == 0):
        ac[question] = 1
        pena += wa[question]
    elif (answer == "WA") and (ac[question] == 0):
        wa[question] += 1

print(sum(ac), pena)