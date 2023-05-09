"""
try 1 : 물건들을 W순으로 정렬한 후,
W가 되는 경우의 Wsum을 result_list에 넣어 max값 반환
-> 런타임 에러
"""
# def add_sum(idx, vsum, wsum):
#     if idx >= N:
#         return
#     if vsum == K:
#         result_list.append(wsum)
#     if vsum >= K:
#         return
#     add_sum(idx + 1, vsum + arr[idx][0], wsum + arr[idx][1])
#
# N, K = map(int, input().split())
# arr = []
# for i in range(N):
#     arr.append(list(map(int, input().split())))
#
# arr.sort(key=lambda x:x[0]) # W값들에 따라서 정렬
# result_list = []
# add_sum(0, 0, 0)
# print(max(result_list))

"""
try 2
찾아보니 배낭 알고리즘이 있음
"""


N, K = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
knapsack = [[0 for _ in range(K+1)] for _ in range(N)]

for i in range(N): # 물건의 개수
    for j in range(K+1): # 들 수 있는 무게의 합
        wsum = arr[i][0]
        vsum = arr[i][1]

        if j < wsum:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], vsum + knapsack[i-1][j-wsum])
            #max(이전에 구해놓은 들수 있는 무게의 합 , 이전에 구해놓은 (들수 있는 무게 - 현재 무게) + 현재 물건 가치)

print(knapsack[N-1][K])
