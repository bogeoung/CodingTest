def sol1():
    N, M = map(int, input().split())

    visited_map = [[0]*M for _ in range(N)]

    input_map = []
    for _ in range(N):
        input_map.append(list(map(int, input())))

    stack = []
    count = 0
    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]
    def dfs(x,y):
        global count
        for i in range(4):
            nx, ny = x + mx[i], y + my[i]
            if nx < 0 or nx + 1 > N or ny < 0 or ny + 1 > M:
                continue
            if input_map[nx][ny] == 0 and visited_map[nx][ny] == 0:
                visited_map[nx][ny] = 1
                dfs(nx,ny)


    for i in range(N):
        for j in range(M):
            if input_map[i][j] == 0 and visited_map[i][j] == 0:
                visited_map[i][j] = 1
                dfs(i,j)
                count += 1
    print(count)


def sol2():
    N, M = map(int, input().split())

    # visited 여부를 다른 자료구조를 생성하는 것이 아니라 1로 표현
    input_map = []
    for _ in range(N):
        input_map.append(list(map(int, input())))

    def dfs2(x,y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return False
        if input_map[x][y] == 0:
            input_map[x][y] = 1
            dfs2(x-1, y)
            dfs2(x+1, y)
            dfs2(x, y-1)
            dfs2(x, y+1)
            return True
        return False

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs2(i, j):
                result += 1
    print(result)

