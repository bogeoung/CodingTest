def solution(new_id):
    def remove_dot(cur_id):
        while cur_id and cur_id[0] == ".":
            cur_id.pop(0)
        while cur_id and cur_id[-1] == ".":
            cur_id.pop()

    answer = ''

    cur_id = []
    # 1,2 단계 실행
    for c in new_id:
        if c == "-" or c == "_" or c == "." or c.isnumeric():
            cur_id.append(c)
        if c.isalpha():
            cur_id.append(c.lower())

    idx = 0
    while True:
        if idx >= len(cur_id) - 2:
            break
        if cur_id[idx] == cur_id[idx + 1] == ".":
            while idx < len(cur_id) - 2 and cur_id[idx + 1] == ".":
                cur_id.pop(idx + 1)
        idx += 1

    remove_dot(cur_id)

    if len(cur_id) == 0:
        cur_id = ["a"]
    elif len(cur_id) >= 16:
        cur_id = cur_id[:15]

    # 마지막에 연속적으로 .이 올것을 대비하여 remove_dot을 썼지만
    # 사실상 앞에서 연속적으로 오는 .을 제거 하였기 때문에
    # 마지막 인덱스의 값만 확인하면 됨.
    remove_dot(cur_id)

    if len(cur_id) <= 2:
        while len(cur_id) < 3:
            cur_id.append(cur_id[-1])

    answer = "".join(cur_id)
    return answer