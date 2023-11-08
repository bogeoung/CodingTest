import sys

N = int(input())
# 입력이 1,000,000까지 들어올 수 있으므로 readline 활용하는 것이 좋을 수 있음
# 마지막 개행이 들어오기 때문에 rstrip 활용하였으나, split 사용시에는 사용 안해도 동일한 결과가 나옴
cur_list = list(map(int, sys.stdin.readline().rstrip().split()))
cur_list.sort()

def find_num(num):
    global cur_list, N
    left = 0
    right = N

    while left <= right:
        mid = (left + right) // 2
        if cur_list[mid] == num:
            return mid
        elif cur_list[mid] < num:
            left = mid + 1
        elif num < cur_list[mid]:
            right = mid - 1
    return None


M = int(input())
number_list = list(map(int, sys.stdin.readline().split()))
for num in number_list:
    if find_num(num) is None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
