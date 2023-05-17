import sys


def input_func():
    N = int(input())
    num_list = list(map(int, input().split()))
    K = int(input())
    return K, sorted(num_list)


def solution(K, num_list):
    inf = sys.maxsize # min으로 값을 업데이트 하기 때문에 maxsize로 배열 초기화
    arr = [inf for _ in range(num_list[-1] * K + 2)]
    arr[1] = 1

    for i in range(1, num_list[-1]*K + 2):
        if i in num_list:
            arr[i] = 1
        else:
            # 두 가지 이상의 수로x 조합되는 경우
            # -> 조건문의 범위가 i//2 + 1이 된다.
            for j in range(1, i//2 + 1):
                arr[i] = min(arr[i], arr[j] + arr[i-j])
        if arr[i] > K:
            if i%2 == 0:
                name = "holsoon"
            else:
                name = "jjaksoon"
            print(f"{name} win at {i}")
            break



def main():
    K, num_list = input_func()
    solution(K, num_list)


if __name__ == '__main__':
    main()

