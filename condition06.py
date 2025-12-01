# 변수를 선언합니다.
score = float(input("점수를 입력하세요: "))

# 조건문을 사용하여 점수에 따른 학점을 출력합니다.
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
else:
    print("재시험")