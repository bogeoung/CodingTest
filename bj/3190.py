from collections import deque

def input_apple(arr):
    asum = int(input())
    for i in range(asum):
        x, y = map(int, input().split())
        arr[x][y] = 9  # 사과 있는 곳은 9로 표현

def input_route():
    # 8 D가 들어오면 8초가 지난 후에 오른쪽으로 튼다는 것으로 입력을 다시 받아야 함.
    route = []
    dir_list = ["right", "down", "left", "up"]
    c_dir = 0
    rsum = int(input())
    for i in range(rsum):
        x, c = input().split()
        if c == "D": # 오른쪽으로 90도 회전
            if c_dir == 3:
                c_dir = 0
            else:
                c_dir += 1
        elif c == "L": # 왼쪽으로 90도 회전
            if c_dir == 0:
                c_dir = 3
            else:
                c_dir -= 1
        route.append([int(x), dir_list[c_dir]])
    return route

def count_sec(arr, route):
    count = 0
    # arr[0][0] = 1 방문 정보를 저장할 필요가 없을 것 같음.
    cur_head_list = deque([[0,0]])
    cur_head = cur_head_list.popleft()
    cur_tail = cur_head # tail = head로 변환하면, 방향성 잃음 -> 수정 필요
    for x_end, c in route:
        for x in range(x_end):
            if c == "right":
                next = [cur_head[0], cur_head[1] + 1]
            elif c == "down":
                next = [cur_head[0] + 1, cur_head[1]]
            elif c == "left":
                next = [cur_head[0], cur_head[1]-1]
            elif c == "up":
                next = [cur_head[0] - 1, cur_head[1]]

            count += 1
            cur_head = next
            cur_head_list.append([cur_head[0], cur_head[1]])

            # arr 밖을 나갔는지 check
            if (cur_head[0] >= len(arr)) or (cur_head[0] < 0):
                return count
            elif (cur_head[1] >= len(arr)) or (cur_head[1] < 0):
                return count
            elif (cur_tail[0] >= len(arr)) or (cur_tail[0] < 0):
                return count
            elif (cur_tail[1] >= len(arr)) or (cur_tail[1] < 0):
                return count

            # 사과가 있는 곳이 아니라면 cur_head_list에서 pop
            if arr[next[0]][next[1]] != 9:
                cur_tail = cur_head_list.popleft()


    return count

def main():
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)] # N X N 배열 생성
    input_apple(arr)
    route = input_route()
    result = count_sec(arr, route)
    print(result)

if __name__ == "__main__":
    main()