from collections import deque

def input_func(N, M):
    arr = [[] for i in range(N + 1)]
    for i in range(M):
        x,y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    # for i in range(N):
    #     arr[i].sort()
    return arr

def bfs(arr, start):
    result = [0 for i in range(len(arr))]
    deq = deque()

    deq.append(start)
    cur_visited=[start]
    while deq:
        cur_num = deq.popleft()
        for i in arr[cur_num]:
            if i not in cur_visited:
                result[i] = result[cur_num] + 1
                cur_visited.append(i)
                deq.append(i)
    return sum(result)


def find_min(arr):
    result = []
    for i in range(1, len(arr)):
        result.append(bfs(arr, i))
    print(result.index(min(result)) +1)

def main():
    N, M = map(int, input().split())
    arr = input_func(N, M)
    find_min(arr)


if __name__ == "__main__":
    main()