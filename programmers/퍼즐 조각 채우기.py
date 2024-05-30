import copy


def print_map(t_name):
    for x in t_name:
        for y in t_name:
            print(t_name[x][y], ends=' ')
        print()


def rearrange(block):
    # (0,0)을 기준으로 좌표 수정
    new_block = copy.copy(block)

    min_x = min(new_block, key=lambda x: x[0])[0]
    min_y = min(new_block, key=lambda x: x[1])[1]

    for i in range(len(new_block)):
        new_block[i][0] -= min_x
        new_block[i][1] -= min_y
    return sorted(new_block)


def rotate(blocks, N):
    rotated_blocks = []
    for b in blocks:
        ny = N - 1 - b[0]
        nx = b[1]
        rotated_blocks.append([nx, ny])
    return sorted(rotated_blocks)


def find_block(table, find_block):
    def dfs(cx, cy, cur_block):
        move_x = [0, 0, 1, -1]
        move_y = [1, -1, 0, 0]

        for mx, my in zip(move_x, move_y):
            nx, ny = cx + mx, cy + my
            # print("new x , new y : ", nx, ny)
            if nx < 0 or nx >= len(table) or ny < 0 or ny >= len(table[0]):
                continue

            if table[nx][ny] == find_block:
                table[nx][ny] = -1
                cur_block.append([nx, ny])
                # print(f"cur_block is updated to {cur_block}")
                dfs(nx, ny, cur_block)

            elif table[nx][ny] != find_block:
                continue

        return cur_block

    block = []
    for x in range(len(table)):
        for y in range(len(table[x])):
            if table[x][y] == find_block:
                table[x][y] = -1
                new_block = dfs(x, y, [[x, y]])

                # 수정된 좌표를 append
                block.append(rearrange(new_block))
    return sorted(block, key=lambda x: -len(x))


def solution(game_board, table):
    answer = 0

    block = find_block(table, 1)
    empty_space = find_block(game_board, 0)

    for space in empty_space:
        if space in block:
            answer += len(space)
            block.remove(space)
        else:
            is_filled = False
            for b in block:
                temp_b = copy.copy(b)
                for _ in range(4):
                    temp_b = rotate(temp_b, len(table))
                    temp_b = rearrange(temp_b)
                    if space == temp_b:
                        answer += len(space)
                        block.remove(b)
                        is_filled = True
                        break
                if is_filled:
                    break

    return answer