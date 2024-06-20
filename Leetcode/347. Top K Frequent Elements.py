from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_list = Counter(nums).most_common(k)
        answer = [item[0] for item in cnt_list]
        return answer