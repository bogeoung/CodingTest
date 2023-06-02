def input_func():
    N = int(input())
    arr = list(map(int, input().split()))
    return N, arr

def solution(N, arr):
    max = 0
    ans = 0
    for i in range(N-1, -1, -1):
        if arr[i] > max:
           max = arr[i]
        else:
            ans += max - arr[i]
    print(ans)

def main():
    T = int(input())
    for i in range(T):
        N, arr = input_func()
        solution(N, arr)


if __name__ == '__main__':
    main()