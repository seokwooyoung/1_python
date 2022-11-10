"""
# 구구단 9단까지 출력

for i in range(1,10):
    for j in range(1,10):
        print(i,'*',j,'=', i*j)
#        print(f'{i} * {j} = {i*j}')
    print('')
"""

# 한 단을 계산하는 함수

def multi(i):
    for j in range(1,10):
        print(f'{i} * {j} = {i*j}')

multi(3)