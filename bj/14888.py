def init_func():
    N = int(input())
    num_arr = list(map(int, input().split()))
    opr_arr = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈
    return num_arr, opr_arr

def opr_func(num1, num2, opr_num):
    if opr_num == 0:
        num1 += num2
    elif opr_num == 1:
        num1 -= num2
    elif opr_num == 2:
        num1 *= num2
    elif opr_num == 3:
        num1 /= num2
    return int(num1)

def solution(n, sum, num_arr, opr_arr):
    global max_num, min_num
    if n == len(num_arr):
        max_num = max(sum, max_num)
        min_num = min(sum, min_num)
    for i in range(4):
        if opr_arr[i] == 0:
            continue
        opr_arr[i] -= 1
        solution(n+1, opr_func(sum, num_arr[n], i), num_arr, opr_arr)
        opr_arr[i] += 1

def main():
    num_arr, opr_arr = init_func()
    global max_num, min_num
    max_num = -1e9
    min_num = 1e9
    solution(1, num_arr[0], num_arr, opr_arr)
    print(max_num)
    print(min_num)
    return

if __name__ == '__main__':
    main()