def input_func():
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(input()))
    return N, M, arr


def is_clue(i,j,arr):
    flag = False
    # 가로
    if j-1 < 0 or arr[i][j-1] != '.':
        if j+2 >= len(arr[i]):
            flag = False
        elif arr[i][j+1] == '.' and arr[i][j+2] == '.':
            return True
    # 세로
    if i-1 < 0 or arr[i-1][j] != '.':
        if i+2 >= len(arr):
            flag = False
        elif arr[i+1][j] == '.' and arr[i+2][j] == '.':
            return True
    return flag


def solution(n, m, arr):
    ans = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#':
                continue
            if arr[i][j] == '.':
                if is_clue(i, j, arr):
                   ans.append([i+1,j+1])

    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])


def main():
    N, M, arr = input_func()
    solution(N, M, arr)


if __name__ == '__main__':
    main()
