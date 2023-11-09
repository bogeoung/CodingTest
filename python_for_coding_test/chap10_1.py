def solution1():
    """
    서로소 집합 알고리즘
    부모 노드를 거슬러 올라가야하므로 노드의 개수가 V, union 연산의 개수가 M개일 때
    전체 시간 복잡도가 O(VM)이 되어 비효율적임.
    """
    def find_parent(parent, x):
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return x

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    v,e = map(int, input().split())
    parent = [0] * (v+1)

    # 자기자신으로 부모 초기화
    for i in range(1, v+1):
        parent[i] = i

    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    print("각 원소가 속한 집합 : ", end = " ")
    for i in range(1, v+1):
        print(find_parent(parent, i), end = " ")
    print()

    print("부모 테이블 : ", end = " ")
    for i in range(1, v+1):
        print(parent[i], end = " ")


def solution2():
    """
    앞선 union_find 알고리즘에 경로 압축 기법을 적용하여 시간복잡도를 낮출 수 있음.
    """
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    # 자기자신으로 부모 초기화
    for i in range(1, v + 1):
        parent[i] = i

    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    print("각 원소가 속한 집합 : ", end=" ")
    for i in range(1, v + 1):
        print(find_parent(parent, i), end=" ")
    print()

    print("부모 테이블 : ", end=" ")
    for i in range(1, v + 1):
        print(parent[i], end=" ")


def solution3():
    """
    서로소 집합을 활용한 사이클 판별 코드
    """
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    v, e = map(int, input().split())
    parent = [0] * (v + 1)

    # 자기자신으로 부모 초기화
    for i in range(1, v + 1):
        parent[i] = i

    cycle = False

    for i in range(e):
        a,b = map(int, input().split())
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            break
        else:
            union_parent(parent, a, b)

    if cycle:
        print("사이클이 발생했습니다.")
    else:
        print("사이클이 발생하지 않았습니다.")


def solution4():
    """
    크루스칼 알고리즘 코드
    간선의 개수가 E개일 때 O(ElogE)의 시간복잡도를 가짐.
    """
    def find_parent(parent,x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    v, e = map(int, input().split())
    parent = [0] * (v+1)

    edges = []
    result = 0
    for i in range(1,v+1):
        parent[i] = i

    for _ in range(e):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    # 간선을 비용순으로 정렬
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)


def solution5():
    """
    위상정렬 코드
    차례대로 모든 노드들을 확인하고 해당 노드에서 출발하는 간선을 제거하기 때문에
    노드와 간선을 모두 확인해서 O(V+E)의 시간복잡도를 가짐.
    """
    from collections import deque

    # 노드의 개수와 간선의 개수 입력받기
    v, e = map(int, input().split())
    # 모든 노드에 대한 진입차수를 0으로 초기화
    indegree = [0] * (v+1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결리스트 초기화
    graph = [[] for _ in range(v+1)]

    # 방향 그래프의 모든 간선 정보 입력 받기
    for i in range(e):
        a,b = map(int, input().split())
        graph[a].append(b) # a와 b가 연결되어 있음을 의미
        indegree[b] += 1   # b와 연결된 노드의 개수를 증가시킴

    # 위상 정렬 함수
    def topology_sort():
        result = []
        q = deque()

        # 진입차수가 0인 노드를 큐에 삽입
        for i in range(1, v+1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            now = q.popleft()
            result.append(now)
            for edge in graph[now]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    q.append(edge)


        # 위상 정렬 수행한 결과 출력
        for i in result:
            print(i, end=" ")

    topology_sort()

solution5()

