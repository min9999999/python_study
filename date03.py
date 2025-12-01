# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜와 시간을 가져옵니다.
now = datetime.datetime.now()

# 봄 구분
if 3 < now.month <= 5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))
    
else :
    print("이번 달은 {}월로 봄이 아닙니다.".format(now.month))