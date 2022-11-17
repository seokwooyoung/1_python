import random

d = dict()

# 한글 문자가 있으므로 encoding='UTF-8' 설정
with open('ko_en.txt', 'rt', encoding='UTF-8') as f:
    for line in f.readlines()[1:]:
        # tap(\t)을 기준으로 k, v로 나눠 저장
        k, v = tuple(line.split('\t'))  
        d[k] = v

quiz = list(d.keys())
# quiz 리스트를 무작위로 섞음
random.shuffle(quiz)

while True:
    # quiz리스트에 남아지 않으면 
    if len(quiz) == 0:
        break
    
    q = quiz.pop()
    print("\nWrite the following sentence in English.")
    print(q)
    a = input("\nyour answer: ")

    # d[q]:문제(=한국어문장) / d[q].rstrip() : 문제에 해당하는 오른쪽 부분(=영어문장)
    if a == d[q].rstrip():
        print('\nresult: Correct!')
    else:
        print("\nresult: Not correct!")
        print("right answer:" + d[q].rstrip() + '\n')

    input()

    print('-' * 80) # 문제 나누기 위함.