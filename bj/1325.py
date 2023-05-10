# pypy로 실행 필요
from collections import deque

def input_func():
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().split())
        arr[y].append(x)
    return arr

def bfs(start, arr):
    count = 1
    deq = deque()
    visited = [False for _ in range(len(arr))]
    visited[start] = True
    deq.append(start)
    while deq:
        next = deq.popleft()
        for j in arr[next]:
            if not visited[j]:
                deq.append(j)
                visited[j] = True
                count += 1
    return count


def solution(arr):
    ans = []
    max_cnt = 0
    for i in range(1, len(arr)):
        cnt = bfs(i, arr)
        if cnt > max_cnt:
            ans.clear()
            max_cnt = cnt
            ans.append(i)
        elif cnt == max_cnt:
            ans.append(i)

    print(*ans)

if __name__ == '__main__':
    arr = input_func()
    solution(arr)