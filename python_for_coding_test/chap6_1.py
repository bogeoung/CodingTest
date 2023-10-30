n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

print(sorted(arr, reverse=True))