from collections import deque
def input_func():
    global M, N
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    for i in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                arr[j][i] = 1
    return arr

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(arr, x, y, count):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < M and 0 <= new_y < N:
                if arr[new_x][new_y] == 0:
                    arr[new_x][new_y] = 1
                    queue.append((new_x, new_y))
                    cnt += 1
    return cnt

def solution(arr):
    ans = []
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 0:
                cnt = bfs(arr, i,j, 0)
                if cnt:
                    ans.append(cnt)

    ans.sort()
    print(len(ans))
    for i in ans:
        print(i, end = ' ')

def main():
    arr = input_func()
    solution(arr)

if __name__ == '__main__':
    main()