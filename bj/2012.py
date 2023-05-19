from collections import deque

def input_func():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))
    return sorted(arr)


def solution(arr):
    ans = 0
    for i in range(len(arr)):
        ans += abs(i + 1 -arr[i])
    print(ans)


def main():
    arr = input_func()
    solution(arr)

if __name__ == '__main__':
    main()