class Solution:
    def dfs(self, cur_node, visited, final_dest):
        global can_path
        global answer

        if cur_node == final_dest:
            answer = True
            return

        # add cur_node to visited
        visited[cur_node] = 1

        for new_node in can_path[cur_node]:
            if visited[new_node] == 0:
                self.dfs(new_node, visited, final_dest)

    def find_can_path(self, edges):
        can_path = {}
        for src, dest in edges:
            if src in can_path.keys():
                can_path[src].append(dest)
            else:
                can_path[src] = [dest]

            if dest in can_path.keys():
                can_path[dest].append(src)
            else:
                can_path[dest] = [src]
        return can_path

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        global can_path
        global answer

        answer = False
        can_path = self.find_can_path(edges)

        visited = [0 for _ in range(n)]
        self.dfs(source, visited, destination)

        return answer
