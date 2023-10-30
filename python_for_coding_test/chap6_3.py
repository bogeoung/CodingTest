N, K = map(int, input().split())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

for i in range(K):
    min_idx = a_arr.index(min(a_arr))
    max_idx = b_arr.index(max(b_arr))

    if a_arr[min_idx] < b_arr[max_idx]:
        a_arr[min_idx], b_arr[max_idx] = b_arr[max_idx], a_arr[min_idx]

print(sum(a_arr))