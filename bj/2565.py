"""
경항성이 중요해 보임.
자기 숫자에서 커지는지, 작아지는지 비교해서 더 작은 값이 잘라야 하는 수 아닌가?
-> 올라가는 거는 올라가는 것끼리, 내려가는 거는 내려가는 것끼리 있다면 옳지 않은 답이 될 돗.
"""
def input_func(num):
    arr = [[] for _ in range(num)]
    for i in range(num):
        n1, n2 = map(int, input().split())
        arr[i] = [n1,n2]
    arr.sort(key = lambda x: x[0]) # 왼쪽 전봇대 기준으로 정렬
    return arr

def solution(arr):
    dp = [1] * len(arr) # 교차되지 않은 전깃줄의 max값
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j][1] < arr[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(len(arr) - max(dp))

def main():
    num = int(input())
    arr = input_func(num)
    solution(arr)

if __name__ == '__main__':
    main()