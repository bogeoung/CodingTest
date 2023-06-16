def input_func():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    return N, K, arr


def solution(N, K, arr):
    ans = []
    for i in range(1, N):
        ans.append(arr[i] - arr[i-1]) # 원생간의 키 차이
    ans.sort(reverse=True) # 내림차순 정렬

    print(sum(ans[K-1:]))


def main():
    N, K, arr = input_func()
    solution(N, K, arr)


if __name__ == '__main__':
    main()