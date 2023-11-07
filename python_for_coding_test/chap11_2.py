num_list = list(map(int, input()))

ans = num_list[0]
for i in range(1, len(num_list)):
    if num_list[i] <= 1 or ans <= 1:
        ans += num_list[i+1]
    else:
        ans *= num_list[i+1]

print(ans)