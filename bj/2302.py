def input_func():
    N = int(input())
    M = int(input())
    arr = []
    for i in range(M):
        arr.append(int(input()))
	# 만약 마지막 좌석이 VIP 좌석이 아닌 경우, N + 1을 VIP arr에 추가해줌.
    if M != 0 and arr[-1] != N:
        arr.append(N + 1)
    return N, M, arr


def make_dp(N):
	# index 0번과 N+1번째를 고려하여 N+2번째까지의 dp를 구해놓는다.
    dp = [0 for _ in range(N + 2)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 2):
        dp[i] = dp[i-1] + dp[i-2]
    return dp


def solution(dp, vips):
    ans = 1
    start = 0
    for vip in vips:
        ans *= dp[vip - 1 - start]
        start = vip
    print(ans)


def main():
    N, M,  arr = input_func()
    dp = make_dp(N)
    if M == 0:
        print(dp[N])
	# N과 M이 같은 경우 모든 좌석이 VIP이기 때문에 답이 1로 고정
    elif N == M:
        print(1)
    else:
        solution(dp, arr)


if __name__ == '__main__':
    main()