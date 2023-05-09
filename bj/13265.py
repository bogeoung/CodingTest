# """
# try 1
# queue를 활용해서 연결돼어있는 노드들을 모두 넣고, 앞에서부터 차례대로 색을 넣되
# 겹치는 색이 있는 순간 바로 impossible return
# -> 굳이 queue에 저장할 필요가 있을까?
# """
#
# def coloring():
#     num_o, num_l = map(int,input().split())
#
#     color = 1
#     colored = [0]*(num_o + 1)
#     for i in range(num_l):
#         num_1, num_2 = map(int,input().split())
#         if (i == 0) and (colored[num_1] == 0):
#             colored[num_1] = color
#             color *= -1
#         if (colored[num_1] == colored[num_2]):
#             print("impossible")
#             return
#         if (colored[num_1] != 0) and (colored[num_2] != 0):
#             continue
#         colored[num_2] = color * -1
#
#     print("possible")
#
#
# n = int(input())
# for i in range(n):
#     coloring()

# """
# try2 : time out
# -> dfs 활용
# """
# def coloring():
#     num_o, num_l = map(int,input().split())
#
#     color = 1
#     colored = {}
#     answer = "possible"
#     for i in range(num_l):
#         num_1, num_2 = map(int,input().split())
#         if num_1 not in colored.keys(): #num1은 없고 num2만 있는 경우는 어떻게..
#             colored[num_1] = color
#         if (num_1 in colored.keys()) and (num_2 in colored.keys()): # 둘다 색이 있는 경우
#             if (colored[num_1] == colored[num_2]):
#                 answer = "impossible"
#             continue
#         colored[num_2] = colored[num_1] * -1
#     print(answer)
#
#
# n = int(input())
# for i in range(n):
#     coloring()

from collections import deque
def bfs(x):
    global result

    que = deque()
    que.append(x)
    colored[x] = 1

    while que:
        cur_num = que.popleft()
        for circle in line_list[cur_num]:
            if colored[circle] == 0:
                colored[circle] = colored[cur_num] * -1
                que.append(circle)
            if colored[circle] == colored[cur_num]:
                result = "impossible"
                return

n = int(input())
for i in range(n):
    num_o, num_l = map(int, input().split())
    line_list = [[] for _ in range(num_o + 1)]
    colored = [0] * (num_o + 1)
    for i in range(num_l):
        n1, n2 = map(int, input().split())
        line_list[n1].append(n2)
        line_list[n2].append(n1)

    result = "possible"

    for i in range(1, num_o + 1):
        if colored[i] == 0:
            bfs(i)
            if result == "impossible":
                break
    print(result)
