n, m = map(int, input().split())

check_map = [[0] * m for _ in range(n)]
cx, cy, direction = map(int, input().split())
check_map[cx][cy] = 1

real_map = []
for i in range(n):
    real_map.append(list(map(int, input().split())))

# 북, 동, 남, 서
mx = [-1, 0, 1, 0]
my = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = cx + mx[direction]
    ny = cy + my[direction]

    # 가보지 않았으며, 땅인 경우
    if check_map[nx][ny] == 0 and real_map[nx][ny] == 0:
        check_map[nx][ny] = 1
        cx, cy = nx, ny
        count += 1
        turn_time = 0
        continue
    else: # 회전만 하는 경우
        turn_time += 1

    # 네방향 다 갈 수 없는 경우
    if turn_time == 4:
        # 바라보던 방향의 뒷칸
        nx = cx - mx[direction]
        ny = cy - my[direction]
        if real_map[nx][ny] == 0:
            cx, cy = nx, ny
            turn_time = 0
        else: # 바다로 막혀있는 경우
            break

print(count)
