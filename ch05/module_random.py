# random 모듈
# random()함수 : 0이상 10미만 숫자 중에 아무 숫자 하나를 뽑음.
import random
print(random.random())

# randrange(a,b) a이상 b미만 중 하나
random.randrange(a, b)

# shuffle() 시퀀스를 뒤죽박죽 섞는 함수
suk = ['a','b','c','d','e']
random.shuffle(suk)
suk     #>> ['a', 'b', 'd', 'c', 'e']
random.shuffle(suk)
suk     #>> ['c', 'e', 'd', 'b', 'a']

# choice() 아무 원소나 하나 뽑아줌
random.choice(suk)

