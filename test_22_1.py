import datetime
now = datetime.datetime.now()

while True:
    Answer = str(input("입력: "))
    if Answer == "안녕":
        print("안녕하세요.")
    elif Answer == "안녕하세요":
        print("안녕하세요.")
    elif Answer == "지금 몇 시야?":
        print(f"지금은 {now.hour}시 {now.minute}분 입니다.")
    elif Answer == "지금 몇 시예요?":
        print(f"지금은 {now.hour}시 {now.minute}분 입니다.")
    elif Answer == "잘 자":
        print("안녕히 주무세요.") 
        break        
    else:
        print(Answer)    


    