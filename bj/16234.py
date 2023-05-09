from collections import deque

def init_func(N):
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    return arr

def bfs(x, y, L, R):
    """
    :param x: 현재 위치 x
    :param y: 현재 위치 y
    :param L, R: L 이상 R이하의 인구수 차이라면 Union
    :return:
    """
    # 인접한 나라의 위치
    d = [(1,0), (0,1), (-1, 0), (0,-1)]
    q = deque()
    N = len(arr)
    union_country = []
    # 현재 위치를 q와 union_country에 추가
    q.append((x,y))
    union_country.append((x,y))

    while q:
        x,y = q.popleft()
        for move_x, move_y in d:
            nx = x + move_x
            ny = y + move_y
            if (0 <= nx < N) and (0 <= ny < N) and not (visited[nx][ny]):
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    union_country.append((nx,ny))
    return union_country

def solution(N, L, R):
    answer = 0
    while True:
        global visited
        visited = [[0]*N for _ in range(N)]
        move = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] = True
                    union_country = bfs(i, j, L, R)
                    if 1 < len(union_country):
                        move = True
                        population = sum([arr[x][y] for x, y in union_country]) // len(union_country)
                        for x, y in union_country:
                            arr[x][y] = population
        # 인구 이동이 일어나지 않은 경우
        if not move:
            break
        # 인구이동이 일어난 경우
        else:
            answer += 1
    print(answer)

def main():
    N, L, R = map(int, input().split())
    global arr
    arr = init_func(N)
    solution(N, L, R)

if __name__=="__main__":
    main()