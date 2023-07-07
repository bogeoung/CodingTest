def input_func():
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    return arr1, arr2


def solution(arr1, arr2):
    init_num = arr2.index(arr1[0])
    case1 = arr2[init_num:] + arr2[:init_num]
    arr2.reverse()
    init_num = arr2.index(arr1[0])
    case2 = arr2[init_num:] + arr2[:init_num]

    if case1 == arr1 or case2 == arr1:
        print("good puzzle")
        return
    print("bad puzzle")
    return


def main():
    arr1, arr2 = input_func()
    solution(arr1, arr2)


if __name__ == '__main__':
    main()
