import sys

sys.setrecursionlimit(int(1e9))

mx = [1, 0, -1, 0]
my = [0, -1, 0, 1]


def dfs(x, y, map, visited):
    global n
    global m

    if x >= n or x < 0 or y >= m or y < 0:
        return 0
    if visited[x][y] == 1:
        return 0
    if map[x][y] == "X":
        return 0

    visited[x][y] = 1
    sum = int(map[x][y])

    for i in range(4):
        nx, ny = x + mx[i], y + my[i]
        sum += dfs(nx, ny, map, visited)

    return sum


def solution(maps):
    answer = []

    # input
    global n  # 행
    global m  # 열

    n = len(maps)
    m = len(maps[0])
    map = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(len(maps[i])):
            map[i][j] = maps[i][j]

    for i in range(n):
        for j in range(len(maps[i])):
            if map[i][j] == "X":
                continue
            else:
                sum = dfs(i, j, map, visited)
                if sum != 0:
                    answer.append(sum)

    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)