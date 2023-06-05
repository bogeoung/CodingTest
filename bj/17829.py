def input_func():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    return arr, N

def solution(arr, N):
    if N == 1:
        print (arr[0][0])
        return
    new_arr = [[] for _ in range(N // 2)]
    for i in range(0,N,2):
        for j in range(0,N,2):
            temp = sorted([arr[i][j], arr[i][j+1],arr[i+1][j],arr[i+1][j+1]])
            new_arr[i//2].append(temp[2])
    return solution(new_arr, N//2)

def main():
    arr, N = input_func()
    solution(arr, N)

if __name__ == '__main__':
    main()