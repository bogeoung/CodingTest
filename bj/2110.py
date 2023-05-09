def init_func(N):
    arr = []
    for i in range(N):
        arr.append(int(input()))
    arr.sort()
    return arr

def solution(arr, c):
    start = 1
    end = arr[-1] - arr[0]
    ans = 0
    while start <= end:
        mid = (end + start) // 2
        cur = arr[0] # 첫 집집에 공유기 두기
        count = 1

        # 현재 mid값의 거리로 공유기 뒀을 때의 공유기 개수
        for i in range(1, len(arr)):
            if arr[i] >= cur + mid:
                count += 1
                cur = arr[i]

        # 공유기 개수 확인
        if count >= c:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    print(ans)

def main():
    N, C = map(int, input().split())
    arr = init_func(N)
    solution(arr, C)

if __name__=="__main__":
    main()