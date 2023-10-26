def sol1():
    N = int(input())
    plan = list(input().split())

    curx, cury = 1, 1

    for p in plan:
        if p == "R" and cury + 1 < N:
            cury += 1
        if p == "L" and cury - 1 > 1:
            cury -= 1
        if p == "U" and curx - 1 > 1:
            curx -= 1
        if p == "D" and curx + 1 < N:
            curx += 1

    print(curx, cury)

def sol2():
    N = int(input())
    plan = input().split()
    x, y = 1,1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    move_types = ['R', 'L', 'D', 'U']
    for p in plan:
        for i in range(len(move_types)):
            if move_types[i] == p:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or nx > N or ny < 1 or ny > N:
            continue

        x,y = nx, ny

    print(x, y)
