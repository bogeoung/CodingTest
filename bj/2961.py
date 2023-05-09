import sys
def input_func(N):
    sum_1, mul_2 = [], []
    for i in range(N+1):
        x,y = map(int, input().split())
        sum_1.append(x)
        mul_2.append(y)


    return sum_1, mul_2

def calculate(arr1, arr2):
    min = sys.maxsize
    for i in range(1,len(arr1)):
        cur_sum = abs(arr1[i] - arr2[i])
        if cur_sum < min:
            min = cur_sum
    print(min)


def main():
    N = int(input())
    arr1, arr2 = input_func(N)
    calculate(arr1, arr2)

if __name__ == "__main__":
    main()