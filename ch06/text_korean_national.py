# out.txt에 애국가 1절~4절 출력
import os
import glob

# 문자열로 인식 
outfile = open('C:\\Users\\HP\\Desktop\\python\\ch06\\korean_national_total.txt', 'wt', encoding='UTF-8')
#outfile = open(r'C:\Users\HP\Desktop\python\ch06\korean_national_total.txt', 'wt', encoding='UTF-8')

for i in glob.glob('korean_national_?.txt'):
    infile = open(i, 'rt', encoding='UTF-8')

    outfile.write(i + '\n')
    outfile.write('-'*30 + '\n')
    outfile.write(infile.read() + '\n\n\n')

outfile.close()
