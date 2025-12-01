# 입력을 받습니다.
num = input("정수 입력> ")

try:
    # 입력한 값을 정수로 변환합니다.
    num = int(num)

    if num % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")
        
except ValueError:
    print("정수를 입력해주세요.")