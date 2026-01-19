# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "과일",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 존재하지 않는 키에 접근해 봅니다.
value = input("접근할 키를 입력하세요: ")

# None 확인 방법
if value not in dictionary:
    print("존재하지 않는 키에 접근했었습니다.")
else:
    print("값:", value, " ", dictionary[value])