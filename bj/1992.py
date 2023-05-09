import sys
input = sys.stdin.readline

n = int(input())
arr = [input() for _ in range(n)]

def quad_tree(cur_x, cur_y, num):
    cur = arr[cur_x][cur_y]
    for i in range(cur_x, cur_x + num):
        for j in range(cur_y, cur_y + num):
            if cur != arr[i][j]:
                print("(", end="")
                quad_tree(cur_x, cur_y, num//2)
                quad_tree(cur_x,cur_y + num//2, num//2 )
                quad_tree(cur_x + num//2, cur_y, num//2)
                quad_tree(cur_x + num//2, cur_y + num//2, num//2)
                print(")", end="")
                return
    if cur == '0':
        print("0", end="")
        return
    if cur == '1':
        print("1", end="")


quad_tree(0, 0, n)