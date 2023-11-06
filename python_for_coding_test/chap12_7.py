# 7. 럭키 스트레이트
# 입력을 스트링으로 받아 자리수를 리스트에 넣고, 리스트 중간 기준으로 양옆의 합이 같은지 확인하기

number_list = list(map(int, input()))
center_idx = len(number_list) // 2

sum1, sum2 = 0, 0
for idx, num in enumerate(number_list):
    if idx < center_idx:
        sum1 += num
    else:
        sum2 += num

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")


