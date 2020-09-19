# 行数
N = int(input().strip())

# 2次元配列
grid = []
for i in range(N):
    array = list(map(int, input().strip().split()))
    grid.append(array)
# print(grid)
counter = 0
frag = False
for i in range(N):
    if grid[i][0] == grid[i][1]:
        counter += 1
        if counter == 3:
            frag = True
    elif grid[i][0] != grid[i][1]:
        counter = 0
if frag is True:
    print("Yes")
else:
    print("No")


