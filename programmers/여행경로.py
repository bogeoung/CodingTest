import copy


def dfs(idx, tickets, visited, visited_name):
    global answer

    dest = tickets[idx][1]

    visited.append(idx)
    visited_name.append(dest)

    if len(visited) == len(tickets):
        answer.append(copy.copy(visited_name))
        return

    for i in range(len(tickets)):
        if i in visited:
            continue
        elif tickets[i][0] == dest:
            dfs(i, tickets, visited, visited_name)
            visited.pop()
            visited_name.pop()


def solution(tickets):
    global answer
    answer = []

    for i in range(len(tickets)):
        visited = []
        visited_name = ["ICN"]
        if tickets[i][0] == "ICN":
            dfs(i, tickets, visited, visited_name)

    answer.sort()

    return answer[0]