def sol1():
    N, M, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    num_list.sort(reverse=True)

    total_num = 0
    for i in range(M):
        if i % K == 0 and i != 0:
            total_num += num_list[1]
        else:
            total_num += num_list[0]

    print(total_num)

def sol2():
    N, M, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    num_list.sort(reverse=True)
    first = num_list[0]
    second = num_list[1]

    times = M // (K+1) # 몫
    remain = M % (K+1) # 나머지

    first_total_count = times * K + remain
    second_total_count = M - first_total_count

    ans = first_total_count * first + second_total_count * second
    print(ans)
