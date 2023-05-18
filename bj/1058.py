def input_func():
    N = int(input())
    arr = []
    for i in range(N):
        # input.split()을 하지 않으면 한 글자씩 분리하여 저장
        arr.append(list(input()))
    return N, arr


def solution(N, arr):
    friend_num = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if j == k:
                    continue
                if arr[j][k] == 'Y' or (arr[j][i] == 'Y' and arr[i][k] == 'Y'):
                    friend_num[j][k] = 1

    ans = 0
    for row in friend_num:
        ans = max(ans, sum(row))
    print(ans)


def main():
    N, arr = input_func()
    solution(N, arr)
    return


if __name__ == '__main__':
    main()
