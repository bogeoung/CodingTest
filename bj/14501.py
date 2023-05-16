from collections import deque

def input_func():
    N = int(input())
    arr = deque()
    for i in range(N):
        t, p = map(int, input().split())
        arr.append([t,p])
    return arr

def solution(arr):
    N = len(arr)
    result = [0 for i in range(N + 1)]
    for i in range(len(arr)):
        # i번째 상담을 했을 때 상담기간 내에 끝나는 날만 확인
        for j in range(i + arr[i][0], N + 1):
            # j를 기준으로 상담했을 때, 얻는 최대 수익 저장
            if result[j] < result[i] + arr[i][1]:
                result[j] = result[i] + arr[i][1]
    print(result[-1])

def main():
    arr = input_func()
    solution(arr)
    return

if __name__ == '__main__':
    main()