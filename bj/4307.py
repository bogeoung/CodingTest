def solution():
    st_len, ant_n = map(int, input().split())

    min_time = []
    max_time = []
    for i in range(ant_n):
        ant = int(input())
        min_time.append(min(ant, st_len - ant))
        max_time.append(max(ant, st_len - ant))

    print(max(min_time), max(max_time))

def main():
    t = int(input())
    for i in range(t):
        solution()


if __name__ == '__main__':
    main()