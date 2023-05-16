def input_func():
    N, K = map(int, input().split())
    L_list = [0] + list(map(int, input().split()))
    return N, K, L_list

def solution(n, k, l_list):
    result = [[0 for _ in range(len(l_list))] for _ in range(2)]
    # result[0] : 점프를 하지 않은 경우
    # result[1] : 점프를 한 경우
    result[0][0] = 1
    result[1][0] = 1
    max = 0
    for i in range(len(l_list)):
        if l_list[i] <= k: # 이동 가능한 경우
            result[0][i] = result[0][i-1] + 1
            result[1][i] = result[1][i-1] + 1
        else: # 이동 불가능한 경우
            result[0][i] = 1
            result[1][i] = result[0][i-1] + 1

        # 최대값 저장
        if result[0][i] > max:
            max = result[0][i]
        if result[1][i] > max:
            max = result[1][i]
    print(max)


def main():
    n, k, l_list = input_func()
    solution(n, k, l_list)

if __name__ == '__main__':
    main()