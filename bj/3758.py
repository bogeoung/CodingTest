def input_func():
    n, k, t, m = map(int, input().split())
    arr = [[0]*k for _ in range(n)]
    time = [0] * n # 마지막 제출 시간 저장
    count = [0] * n # 제출 횟수 저장
    for idx in range(m):
        i, j, s = map(int, input().split()) # id, 문제번호, 점수
        arr[i-1][j-1] = max(arr[i-1][j-1], s)
        time[i-1] = idx
        count[i-1] += 1
    return t, arr, time, count


def solution(t, arr, time, count):
    n = len(arr) # 팀의 개수
    score_list = []
    for idx in range(n):
        score_list.append([sum(arr[idx]), count[idx], time[idx], idx]) # 순위에 맞게 정렬을 할 것이기 때문에 팀번호 idx도 저장
    score_list.sort(key=lambda x: (-x[0], x[1], x[2])) # 정렬
    for idx in range(n):
        if score_list[idx][3] == t-1:
            print(idx+1)
            return


def main():
    T = int(input())
    for i in range(T):
        t, arr, time, count = input_func()
        solution(t, arr, time, count)


if __name__ == '__main__':
    main()
