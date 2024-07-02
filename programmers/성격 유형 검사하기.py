def solution(survey, choices):
    answer = {"R": 0, "T": 0,
              "C": 0, "F": 0,
              "J": 0, "M": 0,
              "A": 0, "N": 0}
    type_answer = ""

    for choice, surv in zip(choices, survey):
        if choice == 4:
            continue
        elif choice < 4:
            answer[surv[0]] += abs(choice - 4)
        else:
            answer[surv[1]] += abs(choice - 4)

    types = list(answer.keys())
    values = list(answer.values())

    for i in range(0, len(answer), 2):
        c1 = values[i]
        c2 = values[i + 1]
        if c1 < c2:
            type_answer += types[i + 1]
        else:
            type_answer += types[i]

    return type_answer