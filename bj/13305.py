def input_func():
    nation_num = int(input())
    num_arr = list(map(int, input().split()))
    nat_arr = list(map(int, input().split()))
    return num_arr, nat_arr


def main(num_arr, nat_arr):
    cheap = nat_arr[0]
    total_cost = cheap * num_arr[0]

    for i in range(1, len(nat_arr) - 1):
        if nat_arr[i] < cheap:
            cheap = nat_arr[i]
        total_cost += cheap * num_arr[i]

    print(total_cost)
    return


if __name__ == "__main__":
    num_arr, nat_arr = input_func()
    main(num_arr, nat_arr)