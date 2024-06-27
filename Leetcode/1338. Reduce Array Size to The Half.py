import heapq
from collections import defaultdict


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_list = defaultdict(int)
        for num in arr:
            count_list[num] += 1

        heap = []
        for key, items in count_list.items():
            heapq.heappush(heap, -items)

        cnt = 0
        target_num = len(arr) // 2
        for i in range(len(heap)):
            cnt += -(heapq.heappop(heap))
            if cnt >= target_num:
                return i + 1