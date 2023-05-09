def dp(start, end, arr):
    for i in range(start, end + 1):
        arr[i] = arr[i-1] + 1
        if i % 2 == 0:
            arr[i] = min(arr[i], arr[i//2]+1)
        if i % 3 == 0:
            arr[i] = min(arr[i], arr[i//3]+1)
    print(arr[end])

def main():
    n = int(input())
    arr = [0] * (n + 1) # 모든 arr의 초기값을 0으로 설정
    dp(2, n, arr)

if __name__ == "__main__":
    main()