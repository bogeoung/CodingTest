class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min = 0
        max = 0

        # 누적합 중 최소와 최댓값을 찾음
        cur_num = 0
        for diff in differences:
            cur_num += diff
            if cur_num < min:
                min = cur_num
            elif cur_num > max:
                max = cur_num

        # lower와 upper 기준으로 min, max값 업데이트
        max = upper - max
        if (lower > 0 and min < 0) or (lower < 0 and min < 0):
            min = lower + -(min)
        else:
            min = lower + min

        if min > max:
            return 0
        else:
            return max - min + 1
