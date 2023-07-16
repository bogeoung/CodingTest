def solution(idx):
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    elif idx % 2 == 0:
        return solution(idx // 2)
    else:
        return 1 - solution(idx // 2)


def main():
    k = int(input())
    print(solution(k-1))


if __name__ == '__main__':
    main()