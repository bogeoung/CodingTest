n = int(input())

arr = []

for _ in range(n):
    name, age = input().split()
    arr.append((name,int(age)))

array = sorted(arr, key=lambda x: x[1])

for student in array:
    print(student[0], end=' ')