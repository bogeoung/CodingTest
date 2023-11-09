N = int(input())
input_list = list(map(int, input().split()))

dp = [0] * 101
dp[0], dp[1] = input_list[0], max(input_list[0], input_list[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + input_list[i])

print(dp[N-1])
