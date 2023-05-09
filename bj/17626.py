def main():
    n = int(input())
    n_list = [0] * (n + 1)
    n_list[1] = 1
    for i in range(2, n + 1):
        j = 1
        min_v = 4
        while (j ** 2) <= i:
            temp = n_list[i - (j ** 2)]
            min_v = min(min_v, temp)
            j += 1
        n_list[i] = min_v + 1
    print(n_list[n])

if __name__=="__main__":
    main()