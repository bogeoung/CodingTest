def sol1():
    N, M = map(int, input().split())
    min_num = 0

    for _ in range(N):
        arr = list(map(int, input().split()))
        cur_row_min = min(arr)
        if cur_row_min > min_num:
            min_num = cur_row_min

    print(min_num)

