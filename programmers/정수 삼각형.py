def solution(triangle):
    for i in range(1, len(triangle)):  # 행
        for j in range(len(triangle[i])):  # 열
            if j == 0:
                triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
            else:
                triangle[i][j] = max(triangle[i - 1][j], triangle[i - 1][j - 1]) + triangle[i][j]

    answer = max(triangle[-1])

    return answer