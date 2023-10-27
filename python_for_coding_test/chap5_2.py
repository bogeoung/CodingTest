from collections import deque
N, M = map(int, input().split())

input_map = []
for _ in range(N):
    input_map.append(list(map(int,input())))

mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

def bfs(x,y):
     queue = deque()
     queue.append((x,y))
     while queue:
         x,y = queue.popleft()
         for i in range(4):
             nx, ny = x + mx[i], y + my[i]
             if nx < 0 or nx >= N or ny < 0 or ny >= M:
                 continue
             if input_map[nx][ny] == 0:
                 continue
             elif input_map[nx][ny] == 1:
                 input_map[nx][ny] = input_map[x][y] + 1
                 queue.append((nx,ny))

     return input_map[N-1][M-1]

print(bfs(0,0))
