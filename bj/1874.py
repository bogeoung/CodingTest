def input_func():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    return n, arr


def solution(n, arr):
    cur_num = 1
    stack_arr = []
    ans = []
    for i in range(n):
        num = arr[i]
        while cur_num <= num:
            stack_arr.append(cur_num)
            ans.append("+")
            cur_num += 1

        if stack_arr[-1] == num:
            stack_arr.pop()
            ans.append("-")
        else: # stack_arr[-1]이 num(뽑아야 할 숫자가)보다 큰경우
            print("NO")
            return

    for calc in ans:
        print(calc)


def main():
    n, arr = input_func()
    solution(n, arr)


if __name__ == '__main__':
    main()