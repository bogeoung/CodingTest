def solution(citations):
    answer = 0
    citations.sort(reverse = True)

    for h in range(len(citations)+1): # 인용된 횟수
        over_h = 0
        for j in range(len(citations)):
            if citations[j] >= h:
                over_h += 1
            else:
                break
        if over_h >= h:
            answer = h
    return answer