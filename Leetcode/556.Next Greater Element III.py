from itertools import permutations

class Solution:
    def nextGreaterElement(self, n: int) -> int:

        n_list = list(str(n))
        n_list.sort()

        perm = permutations(n_list, len(n_list))

        max_int = 2 ** 31 - 1
        can_list = []
        for p in perm:
            temp = int(''.join(p))
            if temp <= max_int and temp > n:
                can_list.append(temp)

        for can in can_list:
            if can > n and can != n:
                return can

        return -1