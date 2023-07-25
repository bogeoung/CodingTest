import sys
input = sys.stdin.readline

def input_func():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    return N, arr


def solution(n, _arr):
    arr = sorted(_arr, key=lambda  x:(x[0]))
    ans = 1
    top = arr[0][1] # 무조건 합격하는 지원자
    for i in range(1,n):
        if arr[i][1] < top:
            top = arr[i][1]
            ans += 1
    print(ans)


def main():
    T = int(input())
    for i in range(T):
        n, arr = input_func()
        solution(n, arr)


if __name__ == '__main__':
    main()