def input_func(N, M):
    arr = [[[] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int,input().split()))
    return arr

def solution(map, N, M):
    ans = 0
    dir_list = [[1,0], [-1,0], [0,1], [0, -1]]

    for i in range(N):
        for j in range(M):
            if not map[i][j]: # 빈 공간일 때만 listed에 넣어 주위 탐방
                ans += 1
                listed = [[i,j]]
                while listed:
                    x, y = listed.pop()
                    for a,b in dir_list:
                        new_x = (x + a) % N
                        new_y = (y + b) % M

                        if not map[new_x][new_y]: # 0 (빈공간)이라면
                            listed.append([new_x,new_y])
                            map[new_x][new_y] = 1
    print(ans)

def main():
    N, M = map(int, input().split())
    map_list = input_func(N, M)
    solution(map_list, N, M)

if __name__ == '__main__':
    main()