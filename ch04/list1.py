"""
# 각 자리 숫자의 합을 계산 sumOfDigits()함수

def sumOfDigits(num):
    sum = 0
    for i in list(str(num)):
        sum = sum + int(i)
    return sum

sumOfDigits(123)
#>> 6
"""
"""
# 줄기와 잎 그림 형식

stem_leaf=[[],[],[]]
score=[0,0,2,4,7,7,9,11,11,13,18,20]

#score[0~6] score[7~10] score[11]
a_score=score[:7]
b_score=score[7:11]
c_score=score[11]
"""
# 풀이
score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]

stem_leaf = [[], [], []]

# ex 1
# 10으로 나눴을 때 몫(d)과 나머지(m) [divmod]
for i in score:
    d, m = divmod(i, 10)
    stem_leaf[d].append(m)

# ex 2
# 몫에 따라 따로 출력
for i in range(len(stem_leaf)):
    print(f'{i}: {stem_leaf[i]}')