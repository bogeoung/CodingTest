from itertools import combinations
def solution(word):
    answer = 0

    full_list = []
    for i in range(1,6):
        alp_list = ["A", "E", "I", "O", "U"] * i
        comb = combinations(alp_list, i)
        for c in comb:
            full_list.append(''.join(c))

    full_set = set(full_list)
    full_list = list(full_set)
    full_list.sort()

    answer = full_list.index(word) + 1

    return answer