from collections import deque

def input_func():
    global n, w, L
    n,w,L = map(int, input().split())
    truck_list = deque(map(int, input().split()))
    return truck_list

def solution(truck_list):
    bridge = deque([0] * w) # 기본은 다리 위를 모두 0으로 채움
    time_count = 0

    while truck_list:
        time_count += 1
        bridge.popleft() # 다리 맨 앞을 제거
        # if truck_count == n:

        if truck_list: # 트럭이 존재하는 동안
            if sum(bridge) + truck_list[0] <= L:
                truck = truck_list.popleft()
                bridge.append(truck)
            else: # 무게가 무거워서 트럭을 추가하지 못하는 경우 0을 넣어 다리 길이 유지
                bridge.append(0)

    # 마지막 트럭이 다리 건너는데 걸리는 시간
    time_count += w

    print(time_count)



def main():
    truck_list = input_func()
    solution(truck_list)
    return


if __name__ == '__main__':
    main()