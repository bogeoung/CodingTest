import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        answer, sum_list, sum_heap = [], [], []

        for row in mat:
            heapq.heappush(sum_heap, sum(row))
            sum_list.append(sum(row))

        for i in range(k):
            min_num = heapq.heappop(sum_heap)
            idx = sum_list.index(min_num)
            answer.append(idx)
            sum_list[idx] = -1

        return answer