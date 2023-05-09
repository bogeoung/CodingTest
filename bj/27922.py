def find_max(N, K):
    sum_12 = []
    sum_23 = []
    sum_13 = []
    for i in range(N):
        x,y,z = map(int, input().split())
        # 3개의 역량 중 2개의 역량을 골랐을 때의 합을 각 arr에 저장
        sum_12.append(x+y)
        sum_23.append(y+z)
        sum_13.append(x+z)

    # 2개의 역량의 합 중 가장 큰 것을 찾기 위해 정렬
    sum_12.sort()
    sum_23.sort()
    sum_13.sort()

    """
    max_12에는 각 강의들의 1,2역량의 합이 저장되어 있음.
    여기서 k개의 강의를 듣는다고 했을 때 정렬 후, 큰 값 k개들의 합을 구하면
    어떤 강의를 듣는지는 모르지만 1,2역량으로 얻을 수 있는 가장 큰 값을 얻을 수 있음.
    max_23, max_13도 동일
    """
    max_12 = sum(sum_12[-K : ])
    max_23 = sum(sum_23[-K : ])
    max_13 = sum(sum_13[-K : ])

    """
    앞서 max_12, max_23, max_13에서 구한 값들은 어떤 강의를 듣는지 모른다고 했음.
    이를 몰라도 되는 이유는 어차피 2개의 역량만을 선택할 수 있기 때문.
    따라서 출력으로 max_12, max_23, max_13 중 max값을 통해 
    N개의 과목 중 K개를 들었을 때 3개의 역량 중 2개의 역량으로 얻을 수 있는 최대값을 출력 가능. 
    """
    print(max(max_12, max_23, max_13))

def main():
    N, K = map(int, input().split())
    find_max(N, K)

if __name__ == "__main__":
    main()