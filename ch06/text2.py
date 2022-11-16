# 비밀 메시지
#각 줄의 첫 두 단어를 문장부호 없이 조합하여 문장을 만들어라
import re
import string

f = open('C:\\Users\HP\Desktop\python\postcard.txt')
"""
#0. 포인터를 가장 앞으로
f.seek(0)

#1. 파일 읽기
a = f.read()
print(a)
"""

#2. 본문 추려내기
lines = f.readlines()

#3. 문장부호 제거
for i in lines[3:10]:
    i = i.replace('.','')   #lines[3:10]에서 문장부호 제거 (.)
    i = i.replace(',','')   #lines[3:10]에서 문장부호 제거 (,)
    i = i.replace(':','')   #lines[3:10]에서 문장부호 제거 (:)
    i = i.upper()
    print(i, end='')    #줄바꿈 하지 않기 위해 end=''사용


#4. 대문자로 변환

#string.ascii_uppercase


#5. 비밀 메시지 출력

