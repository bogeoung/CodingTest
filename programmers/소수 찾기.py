import itertools as it

def check_func(ans):
    if ans < 2:
        return False
    for i in range(2, int(ans ** 0.5) + 1):
        if ans % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    number = [n for n in numbers]

    for i in range(1, len(numbers) + 1):
        answer += list(it.permutations(number, i))
    answer = [int("".join(ans)) for ans in answer]

    new_ans = []
    for ans in answer:
        if check_func(ans):
            new_ans.append(ans)

    print(answer)
    return len(set(new_ans))