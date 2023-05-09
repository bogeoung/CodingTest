def input_func(arr, N):
    for i in range(N):
        arr.append(list(map(int, input().split())))


def count_meeting(arr):
    count = 1
    end_time = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][0] >= end_time:
            end_time = arr[i][1]
            count += 1
    return count


def main():
    N = int(input())
    arr = []
    input_func(arr, N)
    arr.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간 기준으로 정렬
    result = count_meeting(arr)
    print(result)


if __name__ == "__main__":
    main()
