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

N, M = map(int, input().split())
parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i

map_list = []
for i in range(M):
    a,b,c = map(int, input().split())
    map_list.append((c,a,b))

map_list.sort()
result = []

for edge in map_list:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result.append(c)

print(sum(result) - max(result))




