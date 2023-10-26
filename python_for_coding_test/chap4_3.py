cur = input().split()

alp_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
curx, cury = 0, int(cur[0][1])

mx = [-2, -2, -1, -1, 1, 1, 2, 2]
my = [-1, 1, -2, 2, -2, 2, -1, 1]

# 출발 위치 받기
for idx, alp in enumerate(alp_list):
    if cur[0][0] == alp:
        curx = idx + 1
        break

count = 0
for i in range(len(mx)):
    nx, ny = curx + mx[i], cury + my[i]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1

print(count)