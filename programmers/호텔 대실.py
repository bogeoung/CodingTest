def solution(book_time):
    room_state = [[], ]

    def room_check(et_hour, et_min):
        if len(room_state) == 1:
            return 0

        new_total = et_hour * 60 + et_min
        for i in range(len(room_state)):
            if i == 0:
                continue
            cur_total = room_state[i][0] * 60 + room_state[i][1]
            if new_total >= cur_total + 10:
                return i
        return -1

    answer = 0
    book_time.sort(key=lambda x: [x[0], x[1]])

    for st, et in book_time:
        st_hour, st_min = int(st[:2]), int(st[3:])
        et_hour, et_min = int(et[:2]), int(et[3:])
        idx = room_check(st_hour, st_min)
        if idx < 0:
            answer += 1
            room_state.append([et_hour, et_min])
        elif idx == 0:
            answer += 1
            room_state.append([et_hour, et_min])
        elif idx > 0:
            room_state[idx] = [et_hour, et_min]

    return answer