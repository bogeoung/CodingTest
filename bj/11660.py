def input_func():
    n, m = map(int, input().split())
    arr, point_arr = [], []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(m):
        point_arr.append(list(map(int, input().split())))
    return n, m, arr, point_arr


def fill_dp(n, arr):
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]
    return dp


def solution(n, m, arr, point_arr):
    dp = fill_dp(n, arr)
    for i in range(m):
        x1, y1, x2, y2 = point_arr[i]
        ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        print(ans)


def main():
    n, m, arr, point_arr = input_func()
    solution(n, m, arr, point_arr)


if __name__ == '__main__':
    main()