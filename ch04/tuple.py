"""
a = 10
b = 20
temp = a    #temp = 10
a = b       #a = 20
b = temp    #b = 10

print(a, b)
"""
"""
def magu_print(x, y, *rest):    # '*'을 붙이면 그 이후에 들어오는 것을 하나의 튜플로 처리
    print(x, y, rest)

magu_print(1,2,3,4,5,6,7,8)
"""

#튜플 p -> 리스트 l
p = (1,2,3)
l = list(p)
print(l)    #[1,2,3]

#리스트 l -> 튜플 p
p = tuple(l)
print(p)    #(1,2,3)

