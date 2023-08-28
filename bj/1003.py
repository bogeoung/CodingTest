def solution():
    global dp

    for i in range(2,41):
        dp[i] = [dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]]


def main(times):
    global dp

    dp = [[] for _ in range(41)]
    dp[0] = [1,0]
    dp[1] = [0,1]

    solution()

    for i in range(times):
        num = int(input())
        print(*dp[num])

    return


if __name__ == '__main__':
    T = int(input())
    main(T)