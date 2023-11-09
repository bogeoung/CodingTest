def solution1():
    """
    n과 m의 범위를 고려하지 않아 시간 초과가 날 확률이 높음
    :return:
    """
    INF = int(1e9)

    N, M, C = map(int, input().split())
    graph = [[INF] * (N+1) for _ in range(N+1)]

    # 자기자신까지의 경로 초기화
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                graph[i][j] = 0

    # 직접적인 통로 입력받기
    for i in range(M):
        x,y,z = map(int, input().split())
        graph[x][y] = z

    # 다익스트라로 어느 한군데 걸러 도착할 수 있는 곳 입력
    for k in range(N+1):
        for a in range(N+1):
            for b in range(N+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    cost_list = []
    nat_count = 0
    for i in range(N+1):
        if C != i and graph[C][i] < INF:
            nat_count += 1
            cost_list.append(graph[C][i])

    print(nat_count, max(cost_list))

def solution2():
    import heapq
    INF = int(1e9)

    N, M, C = map(int, input().split())
    graph = [[] * (N+1) for _ in range(N+1)]
    distance = [INF] * (N+1)

    # 직접적인 통로 입력받기
    for i in range(M):
        x, y, z = map(int, input().split())
        graph[x].append((y,z))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 경우가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra(C)

    count = 0
    max_distance = 0
    for d in distance:
        if d != INF:
            count += 1
            max_distance = max(max_distance, d)
    
    # 시작노드를 제외하기 위해서 count -1 출력
    print(count -1, max_distance)

solution2()