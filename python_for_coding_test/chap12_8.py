input_list = list(input())
num_list, alph_list = [], []

for data in input_list:
    # 아스키 코드로 변환해서 대문자 a와의 비교, isalpha()와 같은 메소드 사용해도 가능
    if ord(data) >= 65:
        alph_list.append(data)
    else:
        num_list.append(data)

alph_list.sort()
num_list.sort()

for alph in alph_list:
    print(alph, end="")
for num in num_list:
    print(num, end="")
