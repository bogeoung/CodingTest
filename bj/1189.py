def input_func():
    R, C, K = map(int, input().split())
    arr = []
    for i in range(R):
        arr.append(list(input()))
    return R, C, K, arr


def dfs(arr, x, y, cur_len):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    global ans
    if (cur_len == k) and (y == c-1) and (x == 0): # 도착지점 도착 확인
        ans += 1
    else:
        arr[x][y] = 'V'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < r) and (0 <= ny < c) and (arr[nx][ny] == '.'):
                arr[nx][ny] = 'V' # 방문했다 가정하고 dfs 진행
                dfs(arr, nx, ny, cur_len + 1)
                arr[nx][ny] = '.' # 원래 상태로 돌린 후 다시 탐색


def main():
    global ans, r, c, k
    r, c, k, arr = input_func()
    ans = 0
    dfs(arr, r-1, 0, 1)
    print(ans)


if __name__ == '__main__':
    main()