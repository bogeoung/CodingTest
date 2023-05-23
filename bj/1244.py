def init_func():
    num_n = int(input())
    switch_list = [0] + list(map(int, input().split()))
    student_n = int(input())
    student_list = []
    for i in range(student_n):
        student_list.append(list(map(int, input().split())))
    return switch_list, student_list

def switch_convert(switch, idx, num):
    if num == 0:
        switch[idx] = 1
    elif num == 1:
        switch[idx] = 0
    return switch

def boy_func(switch, num):
    for idx, n in enumerate(switch): # for문 증감문 활용 가능
        if idx == 0:
            continue
        elif idx % num == 0:
            switch_convert(switch, idx, n)
    return switch

def girl_func(switch, num):
    idx_mul = 1
    switch_convert(switch, num, switch[num])
    while True:
        l_idx, r_idx = num - idx_mul, num + idx_mul
        if l_idx < 1 or r_idx > len(switch) - 1:
            break
        if switch[l_idx] == switch[r_idx]:
            switch_convert(switch, l_idx, switch[l_idx])
            switch_convert(switch, r_idx, switch[r_idx])
            idx_mul += 1
        elif switch[l_idx] != switch[r_idx]:
            break

def solution(switch, student):
    for s in student:
        if s[0] == 1:
            boy_func(switch, s[1])
        elif s[0] == 2:
            girl_func(switch, s[1])
    switch.pop(0)

    for i in range(0, len(switch), 20): #20개마다 개행 추가
        print(*switch[i:i+20])

def main():
    switch, student = init_func()
    solution(switch, student)
    return


if __name__ == '__main__':
    main()