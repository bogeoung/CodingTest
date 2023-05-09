def input_func():
    times = int(input())
    arr = [[] for i in range(times)]
    for i in range(times):
        num, s, b = map(int,input().split())
        arr[i].append(num)
        arr[i].append(s)
        arr[i].append(b)
    return arr

def solution(arr):
    count = 0

    # 123 ~ 789까지의 숫자를 비교
    for i in range(123, 988):
        i = str(i)
        if '0' in i: # 0을 사용하지 않기 때문에 0이 들어가면 비교x
            continue

        flag = False
        for num, s, b in arr:
            s_num = 0
            b_num = 0
            hundred, ten, one = i[0], i[1], i[2]

            # 서로 다른 숫자 세 개로 구성되어있다고 했으므로, 같은 숫자가 있으면 비교 x
            if (hundred == ten) or (ten == one) or (hundred == one):
                continue

            if hundred == num[0]:
                s_num += 1
            elif hundred in num:
                b_num += 1

            if ten == num[1]:
                s_num += 1
            elif ten in num:
                b_num += 1

            if one == num[2]:
                s_num += 1
            elif one in num:
                b_num += 1

            if (s_num == s) and (b_num == b):
                flag = True
            else:
                flag = False
                break

        if flag is True:
            count += 1

    print(count)



def main():
    arr = input_func()
    solution(arr)

if __name__ == "__main__":
    main()