from itertools import permutations

def input_func():
    N, K = map(int, input().split())
    work_list = list(map(int, input().split()))
    return K, work_list


def solution(K, work_list):
    per = list(permutations(work_list))
    ans = 0
    flag = False
    today = 500
    for p in per:
        for num in p:
            today = (today - K) + num
            if today < 500:
                today = 500
                flag = False
                break
            flag = True

        if flag:
            today = 500
            ans += 1

    print(ans)


def main():
    K, work_list = input_func()
    solution(K,work_list)

if __name__ == '__main__':
    main()