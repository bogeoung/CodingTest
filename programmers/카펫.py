def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            j = yellow // i
            h = min(i, j)
            w = max(i, j)

            b_w, b_h = w + 2, h + 2
            if (b_w * b_h) == (yellow + brown):
                answer = [b_w, b_h]
                return sorted(answer, reverse=True)
