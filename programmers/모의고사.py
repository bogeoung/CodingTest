def h_1(answers):
    h_1 = [1, 2, 3, 4, 5]
    h_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    h_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    human = [h_1, h_2, h_3]
    ans = []

    for h in human:
        count = 0
        for i in range(len(answers)):
            if answers[i] == h[i % len(h)]:
                count += 1
        ans.append(count)

    max = 0
    return_value = []
    for i in range(len(ans)):
        if ans[i] > max:
            max = ans[i]
            return_value = []
            return_value.append(i + 1)
        elif ans[i] == max:
            return_value.append(i + 1)

    return return_value


def solution(answers):
    return h_1(answers)