number = input("정수 입력>")

# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_character = int(last_character)

# 짝수/홀수 판별
if (last_character % 2) == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")