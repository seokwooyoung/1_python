def hap(x, y):
    return x+y

hap(10,5)

# lambda()
# lambda 매개변수 : 표현식
(lambda x,y : x+y)(10,30)
# >> 40

# map()
# map(함수, 리스트)
list(map(lambda x:x**2, range(5)))
# >> [0, 1, 4, 9, 16]

# reduce()
# reduce(함수, 시퀀스)
from functools import reduce
reduce(lambda x, y: x+y, [0, 1, 2, 3, 4])
# 0과 1을 더하고, 그 결과에 2를 더하고, 그 결과에 3을 더하고...
# >> 10
reduce(lambda x, y: x+y, 'abcde')
# >> abcde
reduce(lambda x, y: y+x, 'abcde')
# >> edcba

# filter()
# filter(함수, 리스트)
list(filter(lambda x: x<5, range(10)))
# >> [0, 1, 2, 3, 4]