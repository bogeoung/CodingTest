"""
2839. 설탕배달
3kg, 5kg 봉지가 있음.
Nkg 배달 시 최대한 적은 봉지를 가져가려 함.
3 <= N <= 5000
"""

def main():
    n = int(input())
    max5 = n // 5
    ans = 0

    for i in range(max5, -1, -1):
        remain = n - (i * 5)
        if remain % 3 == 0:
            ans = i + remain // 3
            break
        # N을 정확하게 만들지 못하는 경우
        if (i == 0) and (n % 3 != 0):
            print("-1")
            return

    print(ans)


if __name__ == '__main__':
    main()