def solution(N, K, A, B):
    arr = [K] * N
    day = 0
    while 0 not in arr:
        for i in range(A):
            arr[i] += B

        for i in range(N): # 물을 준 화분도 수분이 감소함
            arr[i] -= 1
        arr.sort() # 모든 캣닢이 살아있는 기간이 최대한 길어저야 하기 때문에 sort
        day += 1
    return day


def main():
    N, K, A, B = map(int, input().split())
    ans = solution(N, K, A, B)
    print(ans)

if __name__ == "__main__":
    main()
