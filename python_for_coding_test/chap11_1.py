# 1. 모험가 길드
# 공포도가 낮은 것부터 채워나가기

N = int(input())
person_list = list(map(int, input().split()))
person_list.sort()

ans = 0 # 결성된 그룹의 개수
cur_num = 0 # 현재 그룹의 인원

for i in person_list:
    cur_num += 1
    if cur_num >= i:
        ans += 1
        cur_num = 0

print(ans)