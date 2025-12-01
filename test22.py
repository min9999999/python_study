str_input = input("태어난 해를 입력해 주세요> ")
birth_year = int(str_input)

if (birth_year % 12) == 0:
    print("원숭이띠")
elif (birth_year % 12) == 1:
    print("닭띠")
elif (birth_year % 12) == 2:
    print("개띠")
elif (birth_year % 12) == 3:
    print("돼지띠")
else:
    print("쥐, 소, 호랑이, 토끼, 용, 뱀, 말, 양띠 중 하나입니다.")