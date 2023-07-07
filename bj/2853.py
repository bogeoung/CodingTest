def input_func():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    return N, arr


def solution(N,arr):
    ans = 0
    for i in range(1, N):
        if arr[i] == 0: # 이미 어떤 boat로 세어짐
            continue
        diff = arr[i] - arr[0]
        temp_cnt = 1
        for j in range(1, N):
            if arr[j] == 0:
                continue
            if arr[j] % diff == 1:
                arr[j] = 0
                temp_cnt += 1
        if temp_cnt != 1:
            ans += 1
    print(ans)


def main():
    N, arr = input_func()
    solution(N, arr)


if __name__ == '__main__':
    main()