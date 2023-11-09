
def solution1():
    """
    간단한 다익스트라 알고리즘
    시간 복잡도가 O(V^2)이라서 전체 노드의 개수가 10,000개가 넘어가면 시간 초과가 나옴.
    일반적으로는 노드의 개수가 5000개 이하일때 사용 가능
    """
    import sys
    input = sys.stdin.readline # () 안붙이도록 주의
    INF = int(1e9)

    # 노드의 개수, 간선의 개수 입력
    n, m = map(int, input().split())
    # 시작 노드 번호 입력
    start = int(input())
    # 각 노드에 연결되어 있는 노드에 대한 정보를 저장하는 리스트
    graph = [[] for i in range(n+1)]
    # 방문 여부 확인하는 리스트
    visited = [False] * (n+1)
    # 최단 거리 테이블 초기화
    distance = [INF] * (n+1)

    # 모든 간선 정보 입력받기
    for _ in range(m):
        a,b,c = map(int, input().split())
        graph[a].append((b,c))

    # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호 반환
    def get_smallest_node():
        min_val = INF
        idx = 0
        for i in range(1, n+1):
            if distance[i] < min_val and not visited[i]:
                min_val = distance[i]
                idx = i
        return idx

    def dijkstra(start):
        # 시작 노드에 대해 초기화
        distance[start] = 0
        visited[start] = True
        for j in graph[start]:
            distance[j[0]] = j[1] # 노드 b까지의 거리는 c

        # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
        for i in range(n-1):
            # 현재 최단 거리가 가장 짧은 노드를 꺼내 방문처리
            now = get_smallest_node()
            visited[now] = True
            # 현재 노드와 연결된 다른 노드를 확인
            for j in graph[now]:
                cost = distance[now] + j[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    # 시작노드서부터 다익스트라 적용
    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리 출력
    for i in range(1, n + 1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])


def solution2():
    """
    개선된 다익스트라 알고리즘
    힙을 사용함으로써 시간복잡도가 O(ElogV)가 됨.
    """

    import sys
    import heapq
    input = sys.stdin.readline
    INF = int(1e9)

    # 노드의 개수, 간선의 개수 입력받기
    n, m = map(int, input().split())
    # 시작 노드 입력받기
    start = int(input())

    graph = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    # 간선 정보 입력받기
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    def dijkstara(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
        # heapq.heappush(저장할 힙, 저장할데이터)
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            # 현재 노드와 연결되어 있는 다른 노드들을 확인
            # i[0]은 노드명, i[1]은 비용
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstara(start)

    for i in range(1, n + 1):
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])


def solution3():
    # 플로이드 워셜 알고리즘

    INF = int(1e9)

    n = int(input())
    m = int(input())

    # 2차원 리스트를 만들고, 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로의 비용 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 간선 정보 업데이트
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    # k를 거치고 가는 경로가 더 짧을 경우 업데이트
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 결과 출력
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print("INFINITY", end=" ")
            else:
                print(graph[a][b], end=" ")
        print()