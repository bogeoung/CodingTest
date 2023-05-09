"""
try 1
도형에서 1,2,3,4 의 개수가 모두 동일하면 같은 도형이라 판단
-> 틀린 가정
"""

# def is_identical(repre_count, arr_count):
#     result = "True"
#     if len(repre_count) != len(arr_count):
#         result = "False"
#         return result
#     for direc in repre_count.keys():
#         if repre_count[direc] == arr_count[direc]:
#             continue
#         else:
#             result = "False"
#             return result
#     return result
#
# def count (arr):
#     arr_dict = {1:0, 2:0, 3:0, 4:0}
#     for direc in arr:
#         if direc not in arr_dict.keys():
#             arr_dict[direc] = 1
#         else:
#             arr_dict[direc] += 1
#
#     return arr_dict
#
# n = int(input())
# repre_arr = list(map(int,input().split()))
# repre_count = count(repre_arr)
#
# times = int(input())
# answer_count = 0
# answer_list = []
# for i in range(times):
#     arr = list(map(int, input().split()))
#     arr_count = count(arr)
#     if is_identical(repre_count, arr_count):
#         answer_count += 1
#         answer_list.append(arr)
#
# print(answer_count)
# for arr in answer_list:
#     print(arr)
"""
try 2
시작점을 지정하고, 거기서부터 같으면 같은 도형이라 판단
(시계방향, 반시계방향)
"""
from collections import deque

def convert(x): # 1->3 , 2 -> 4, 3->1, 4-> 1
    if x == 2:
        return 4
    return (x + 2) % 4

def is_identical(arr, repre_arr):
    arr_rev = arr.copy()
    repre_arr_rev = deque(map(convert, repre_arr))
    repre_arr_rev.reverse()

    for _ in range(len(repre_arr)):
        if (arr_rev == repre_arr) or (arr_rev == repre_arr_rev):
            return True
        arr_rev.rotate(1)
    return False

def main():
    n = int(input())
    repre_arr = deque(map(int, input().split()))

    times = int(input())
    answer_list = []
    for i in range(times):
        arr = deque(map(int, input().split()))
        if is_identical(arr, repre_arr):
            answer_list.append(arr)

    print(len(answer_list))
    for l in answer_list:
        print(*list(l))

if __name__ == "__main__":
    main()