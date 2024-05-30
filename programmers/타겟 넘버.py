def dfs(numbers, target, index, total):
    if (index == len(numbers)):
        if (target == total):
            return 1
        return 0
    return dfs(numbers, target, index + 1, total + numbers[index]) + \
        dfs(numbers, target, index + 1, total - numbers[index])


def solution(numbers, target):
    return dfs(numbers, target, 0, 0)