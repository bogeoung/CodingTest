import sys
def input_func(N):
    arr = list((map(int,input().split())))
    arr.sort()
    return arr


def sum_func(arr):
    L = 0
    R = len(arr) - 1
    min = [sys.maxsize, L, R] # 두 용액합의 현재까지의 최소값, L idx, R idx

    while L < R:
        sum = arr[L] + arr[R]
        if sum == 0:
            min[1], min[2] = arr[L], arr[R]
            break
        if abs(sum) < abs(min[0]):
            min[0] = sum
            min[1] = arr[L]
            min[2] = arr[R]
        if sum < 0: # 최소값이 0보다 작음, abs[0]으로 업데이트 되지 않을 수 있으므로 현재 값들의 합 이용
            L += 1
        else: # 최소값이 0보다 크기 때문에
            R -= 1
    print(min[1], min[2])
    return


def main():
    N = int(input())
    arr = input_func(N)
    sum_func(arr)

if __name__=="__main__":
    main()