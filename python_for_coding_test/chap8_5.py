N, M = map(int, input().split())
m_list = []
dp = [10001] * 10001

for i in range(N):
    num = int(input())
    m_list.append(num)
    dp[num] = 1

for i in range(N):
    for j in range(m_list[i], M+1):
        if dp[j - m_list[i]] != -1:
            dp[j] = min(dp[j], dp[j - m_list[i]] +  1)

if dp[M] == 10001:
    print("-1")
else:
    print(dp[M])
