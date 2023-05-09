# arr = []
# visited = []
# N, S = 0, 0
# count = 0
# def make_sum(idx, sum):
#     global count
#     if idx >= N:
#         return
#     if sum == S:
#         count += 1
#     sum += arr[idx]
#     make_sum(idx + 1, sum)
#
# def main():
#     N, S = map(int,input().split())
#     arr = map(int, input().split())
#     make_sum(arr, 0, S)
#
# if __name__ == "__main__":
#     main()

def make_sum(idx, sum):
    global count
    if idx >= N:
        return

    sum += arr[idx] # sum과 S를 비교하기 전에 arr[idx]를 하나라도 더해야만, 원소가 하나도 없는 것을 고려할 수 있음

    if sum == S:
        count += 1

    make_sum(idx + 1, sum)
    make_sum(idx + 1, sum - arr[idx])


N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

make_sum(0, 0)
print(count)

