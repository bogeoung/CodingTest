"""
solution1은 높이 H를 최대값에서부터 줄여가고,
input_list의 값이 H보다 큰 위치서부터 잘린 떡의 길이를 비교함
하지만 H의 범위가 1부터 10억까지의 정수이기 때문에 이런 경우 시간초과가 날 수도 있음(?)
따라서 input_list의 값이 H보다 큰 위치를 구할 때 이진 탐색을 사용하는 것이 아니라,
H의 범위를 이진 탐색으로 줄여나가는 것이 필요
"""
def solution1():
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))

    input_list.sort()

    def find_max(start, end, num):
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            if num <= input_list[mid]:
                for i in range(mid, len(input_list)):
                    ans += input_list[i] - num
                return ans
            elif num < input_list[mid]:
                end = mid -1
            elif num > input_list[mid]:
                start = mid + 1
        return None

    for i in range(input_list[-1], 0, -1):
        if find_max(0, len(input_list)-1, i) >= M:
            print(i)
            break


def solution2():
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_list.sort()

    left, right = 0, input_list[-1]
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        total = 0

        for x in input_list:
            if x > mid:
                total += x - mid
        # 양이 부족해서 H를 낮춰서 더 많이 자르기
        if total < M:
            right = mid - 1
        # 양이 충분해서 H를 높여 더 적게 잘라보기
        else:
            ans = mid
            left = mid + 1

    print(ans)

solution2()



