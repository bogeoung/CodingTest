
def init(n, wires):
    stack = []
    for i in range(0, n+1):
        stack.append([])
    for wire in wires:
        stack[wire[0]].append(wire[1])
        stack[wire[1]].append(wire[0])
    return stack

def dfs(n, start_num, wires, maps, visited):
    stack = []
    ans = 1
    #init stack
    for m in maps[start_num]:
        if m not in visited:
            stack.append((start_num, m))
            visited.append(m)
            ans += 1
    while(stack):
        cur = stack.pop()
        for m in maps[cur[1]]:
            if m not in visited:
                stack.append((cur[1], m))
                visited.append(m)
                ans += 1
    return ans

def solution(n, wires):
    answer = n
    maps = init(n, wires)

    # print(stack)
    for wire in wires:
        visited = []
        visited.append(wire[0])
        visited.append(wire[1])
        temp1 = dfs(n, wire[0], wires, maps, visited)
        temp2 = dfs(n, wire[1], wires, maps, visited)

        answer = min(answer, abs(temp1 - temp2))
    return answer