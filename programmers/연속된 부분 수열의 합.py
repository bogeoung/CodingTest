def solution(sequence, k):
    answer = []
    n = len(sequence)
    r = 0
    sum = 0

    for l in range(n):
        while sum < k and r < n:
            sum += sequence[r]
            r += 1

        if sum == k:
            answer.append([l, r - 1, r - l - 1])
        sum -= sequence[l]

    answer.sort(key=lambda x: x[2])
    return answer[0][:-1]

