"""
import os
os.getcwd()
#>> 'C:\\Users\\HP\\Desktop\\python'

os.listdir()
#>> ['.git', 'ch00', 'ch01', 'ch02', 'ch03', 'ch04', 'ch05', 'ch06', 'hello.txt', 'letter.txt']

# 파일을 처음부터 끝까지 읽기 read()
f = open('hello.txt')
a = f.read()
print(a)
"""
f = open('letter.txt')

# readline() : 파일을 한줄씩 읽기 
#b = f.readline()
#print(b)
"""
f.readline()
#>> 'Dear Father,\n'
f.readline()
#>> '\n'
f.readline()
#>> 'How are you?'
f.readline()
#>> ''
"""
"""
# 5줄 읽기
for i in range(5):
    print(f.readline())
"""

#readlines() : 각 줄이 리스트의 원소로 들어감
c = f.readlines()
print(c[:2])

