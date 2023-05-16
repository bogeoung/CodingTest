import sys

def input_func():
    n, m = map(int, input().split())
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(m):
        x,y = map(int, input().split())
        graph[x][y] = 1 # x,y는 서로 인접한 노드
    return n, graph


def solution(n, graph):
    for i in range(1, n+1): # i를 통해서 연결된 노드들을 다 update
        for j in range(1, n+1):
            for k in range(1, n+1):
                # 가중치가 존재하지 않는 경우 j와 k가 i를 통해서 연결되었을 때 1(연결됨)로 업데이트
                # j와 k가 이미 연결이 되었을 경우 이미 1(연결됨)로 업데이트 되어 있기에 고려 대상이 아님(조건문에 추가할 필요 없음)
                # 가중치가 존재하는 경우 j와 k가 i를 통해서 연결되었을 때 min(graph[j][k], graph[j][i] + graph[i][k])로 업데이트
                if (graph[j][i] == 1) and (graph[i][k] == 1):
                    graph[j][k] = 1
    return graph

def main():
    n, compare_list = input_func()
    ans = 0
    compare_list = solution(n, compare_list)

    for i in range(1,n+1):
        count = 0
        for j in range(1, n+1):
            # i 보다 키가 큰 경우 + i보다 키가 작은 경우의 합과 n-1을 비교
            count += compare_list[i][j] + compare_list[j][i]
        if count == n-1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()