"""
# sys모듈 : 파이썬 인터프리터 제어
import sys

# 현재 프롬포트
sys.ps1
#>> '>> '

sys.ps1 = '^^'
sys.ps1
#^^

# 인터프리터 끝내기
sys.exit()

#############################################

# os모듈 : 운영체제 제어
import os

# 현재 경로
os.getcwd()
#>> 'C:\\Users\\HP\\Desktop\\python'

# 이 경로에 있는 파일들
os.listdir()
#>> ['.git', 'ch00', 'ch01', 'ch02', 'ch03', 'ch04', 'ch05']

# ch05 디렉토리로 이동
os.chdir('ch05')

# 경로
os.getcwd()
#>> 'C:\\Users\\HP\\Desktop\\python\\ch05'

# 이 경로에 있는 파일들
os.listdir()
#>> ['module.py', 'module1.py', 'module_calendar.py', 'module_math.py', 'module_tkinter.py']
"""
#############################################

# 웹브라우저 열기
import webbrowser
url = 'http://www.python.org/'
webbrowser.open(url)