import math

# 2의 제곱근
math.sqrt(2)
#>> 1.4142135...
round(math.sqrt(2),3)
#>> 1.414


# 달력
import calendar

calendar.prmonth(2022,12)
"""
>>    December 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
"""

# import 모듈 : 모듈 전체를 가져오기
import tkinter
tkinter.widget = tkinter.Label(None, text = 'I love python.')
tkinter.widget.pack()

# from 모듈 import 이름 : 모듈 내에서 필요한 것만 가져오기
from tkinter import *
widget = Label(None, text = 'I love python.')
widget.pack()

"""
# 모듈에 무엇이 있는지 알기 위해
import 모듈
dir(모듈)
"""