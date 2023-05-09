def input_func():
    a_num, b_num = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    a_arr.sort()
    b_arr.sort()
    return a_arr, b_arr

def solution(a_arr, b_arr):
    count = 0
    for i in a_arr:
        for j in b_arr:
            if i > j:
                count += 1
            else:
                break
    print(count)

def solution2(a_arr, b_arr):
    count = 0
    for a in a_arr:
        tmp_count = 0
        start, end = 0, len(b_arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if b_arr[mid] < a:
                tmp_count = mid + 1
                start = mid + 1
            else:
                end = mid - 1
        count += tmp_count
    print(count)

def main():
    T = int(input())
    for i in range(T):
        a_arr, b_arr = input_func()
        solution2(a_arr, b_arr)

if __name__ == '__main__':
    main()