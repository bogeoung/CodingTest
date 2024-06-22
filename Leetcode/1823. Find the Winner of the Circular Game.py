class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friend_list = [x for x in range(1, n + 1)]

        cur_idx = 0
        cnt = 1
        while len(friend_list) > 1:
            if cur_idx >= len(friend_list):
                cur_idx = cur_idx % len(friend_list)
            if cnt == k:
                friend_list.pop(cur_idx)
                cnt = 1
            else:
                cnt += 1
                cur_idx += 1

        return friend_list[0]
