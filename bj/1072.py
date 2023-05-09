# """
# try 1
# ans 라는 변수를 두고, 재귀적으로 함수를 호출하면서 새로 구한 win_rate와 기존 win_rate가  비교
# """
# import math
# import sys
# sys.setrecursionlimit(10000)
# def count_play(X, Y, win_rate, count):
#     updated_win_rate = math.trunc((Y / X) * 100)
#     if (win_rate == 100) or (win_rate == 99):
#         print("-1")
#         return count
#
#     if updated_win_rate == win_rate:
#         count += 1
#         count_play(X + 1, Y + 1, win_rate, count) # 여기서 return하면 count가 변경되지 않고 return 됨.
#     else:
#         print(count)
#         """
#         여기서 print하는 것이 아니라 main에서 출력하려고 하면 어떻게 해야할까?
#         재귀때문에 count가 바뀐다.
#         재귀로 호출하는 것 때문에 일부러 count_play(..,count +1) 로 호출하는 것이 안리ㅏ
#         count += 1을 수행한 후 재귀를 호출했는데, 왜 숫자가 주는지 모르겠음.
#         """
#         return
#
# def main():
#     X, Y = map(int, input().split())
#     ans = 1
#     win_rate = math.trunc((Y / X) * 100)
#     count_play(X + 1, Y + 1, win_rate, ans)
#
# if __name__ == "__main__":
#     main()

def count_play(X, Y):
    Z = (Y * 100) // X
    # X = (Y/Z) * 100으로 작성하면 부동소수점 때문에 틀림.
    if Z >= 99: # Z가 99이상이라면 승률은 절대 변하지 않음. 한번이라도 이미 졌기 때문에 절대 100이 될 수 없음.
        print("-1")
        return
    answer = 0
    left = 1 # 시작 인덱스
    right = X # 끝을 나타냄

    while left <= right:
        mid = (left + right) // 2
        # 현재의 승률이 처음 승률보다 작을 경우, 이긴 횟수를 줄여야 함.
        if Z < ((Y+mid)*100 // (X + mid)):
            answer = mid
            right = mid - 1
        # 현재의 승률이 처음 승률보다 크거나 같을 경우, 이긴 횟수 증가해야함.
        else:
            left = mid + 1
    print(answer)

def main():
    X, Y = map(int, input().split())
    count_play(X, Y)


if __name__ == "__main__":
    main()