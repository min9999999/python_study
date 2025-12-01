# 입력을 받습니다.
number = input("정수 입력> ")


try:
    number = int(number)
    # 양수 조건
    if number > 0:
        print("양수입니다.")
        
    # 음수 조건
    if number < 0:
        print("음수입니다.")

    # 0 조건
    if number == 0:
        print("0입니다.")
        
    # 에러 조건
    if not number == int(number):
        print("정수가 아닙니다.")
except ValueError:
    print("정수가 아닙니다.")