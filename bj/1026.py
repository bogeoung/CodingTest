def input_func():
    len = int(input())
    arr_a = map(int, input().split())
    arr_b = map(int, input().split())
    return arr_a, arr_b


def main(arr_tuple):
    arr_a, arr_b = map(list, arr_tuple)
    arr_a.sort(reverse = True)
    arr_b.sort()

    answer = 0
    for a,b in zip(arr_a, arr_b):
        answer += a * b

    print(answer)


if __name__ == '__main__':
    main(input_func())


