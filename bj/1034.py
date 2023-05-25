def input_func():
    N, M = map(int, input().split())
    status = []
    for i in range(N):
        status.append(list(map(int, input())))
    K = int(input())
    return N, K, status


def solution(n, k, status):
    ans = []
    for i in range(n):
        zero_cnt = 0
        for num in status[i]:
            if num == 0:
                zero_cnt += 1
        col_cnt = 0
        if zero_cnt <= k and zero_cnt%2 == k%2:
            for i_2 in range(n):
                if status[i] == status[i_2]:
                    col_cnt += 1
        ans.append(col_cnt)
    print(max(ans))


def main():
    n, k, status = input_func()
    solution(n, k, status)

if __name__ == '__main__':
    main()