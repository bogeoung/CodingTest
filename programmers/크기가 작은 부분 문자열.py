def solution(t, p):
    answer = 0
    n = len(p)

    for i in range(len(t) - n + 1):
        temp = t[i:i + n]
        if int(temp) <= int(p):
            answer += 1
    return answer