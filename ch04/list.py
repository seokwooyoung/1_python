"""
### 문자열 
x = 'banana'

print(x)
#>> banana

y = x[2]+ x[1:6]
print(y)
#>> nanana

a = 'Hello world. suk.'
a.find('s')
#>> 13

b = a[13:16]
print(b)
#>> suk
"""

### 리스트
p = [3,7,11]

# 원소 추가
p.append(5)
print(p)
#>> [3,7,11,5]

# 크기 순 정렬
p.sort()
print(p)
#>> [3,5,7,11]

# 맨 앞(0)에 2 삽입
p.insert(0, 2)
print(p)
#>> [2,3,5,7,11]

# 4번 원소 삭제
del p[4]
print(p)
#>> [2,3,5,7]

#새로운 값 지정
p[0]=1
print(p)
#>> [1,3,5,7]

# 리스트내에 리스트
x = ['potatos',['pizza','coke','salad'],'chicken']
print(x[1][0])
#>> pizza

# 리스트로 변환
list('Hello world.')
#>> ['H','e','l','l','o',' ','w','o','r','l','d','.']

