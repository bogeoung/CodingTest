class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        linked_dict = {}

        for edge in edges:
            if edge[0] in linked_dict.keys():
                linked_dict[edge[0]].append(edge[1])
            else:
                linked_dict[edge[0]] = [edge[1]]
            if edge[1] in linked_dict.keys():
                linked_dict[edge[1]].append(edge[0])
            else:
                linked_dict[edge[1]] = [edge[0]]

        max_len = 0
        max_key = 0
        for key, val in linked_dict.items():
            if len(val) > max_len:
                max_len = len(val)
                max_key = key

        return max_key