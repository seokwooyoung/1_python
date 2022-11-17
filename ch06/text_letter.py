"""
# 파일을 열어 읽기
f = open('C:\\Users\HP\Desktop\python\ch06\hello.txt')
a = f.read()
print(a)

# \n 줄바꿈
print('야호~\n호야\n~')
"""

# 파일에 글쓰기
letter = open('C:\\Users\HP\Desktop\python\ch06\letter.txt', 'w')    #w 
letter.write('Dear Father,')
letter.close
#>> 파일을 열면 Dear Father,가 쓰여진 것을 볼 수 있음.

# 파일에 들어있는 데이터를 지우지 않고 추가 
letter = open('C:\\Users\HP\Desktop\python\ch06\letter.txt', 'a+')   #a+
letter.write('\n\nHow are you?')
letter.close()

letter = open('C:\\Users\HP\Desktop\python\ch06\letter.txt', 'a+')   #a+
letter.write('\n\nWhere are you?')

letter = open('C:\\Users\HP\Desktop\python\ch06\letter.txt', 'a+')   #a+
letter.write('\n\nWhat are you doing?')
letter.close()

