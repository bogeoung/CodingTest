"""
암호는 L개의 소문자, 최소 한개의 모음과 두개의 자음으로 구성
사용될 수 있는 문자의 종류는 C개
"""
from itertools import combinations

def input_func():
    L, C = map(int, input().split())
    arr = input().split()
    arr.sort()
    return L, arr

def solution(L, arr):
    candidate = list(combinations(arr, L))
    for can in candidate:
        not_flag_num = 0
        flag_num = 0
        for word in can:
            if word in "aeiou":
                flag_num += 1
                continue
            not_flag_num += 1
        if flag_num >= 1 and not_flag_num >= 2:
            print(''.join(list(can)))

def main():
    L, arr = input_func()
    solution(L, arr)
    return

if __name__ == '__main__':
    main()