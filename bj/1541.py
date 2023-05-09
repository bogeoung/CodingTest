def input_func():
    arr = input().split("-")
    return arr

def solution(arr):
    ans = 0
    for idx, num in enumerate(arr):
        # 처음 시작 숫자가 음수인경우 고려
        if idx == 0:
            temp = sum(map(int, num.split("+")))
            if num[0] == "-":
                ans -= int(temp)
                continue
            ans += int(temp)
            continue

        temp = sum(map(int, num.split("+")))
        ans -= temp
    print(ans)

def main():
    arr = input_func()
    solution(arr)

if __name__ == '__main__':
    main()