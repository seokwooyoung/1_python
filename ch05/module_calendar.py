"""
# calendar모듈 
import calendar

# 모듈에 무엇이 있나?
help(calendar)

# calendar 모듈에 leap이라는 문자열을 포함하는 이름 
[x for x in der(calendar) if 'leap' in x]

# 해가 윤년인지 아닌지 판별
help(calendar.isleap)

calendar.isleap(2022)
#>> False
"""

# 2021년 2월 달력 = 변수 m으로 저장 -> 화면 출력
import calendar
c = calendar.TextCalendar()
m = c.formatmonth(2021, 2)
print(m)