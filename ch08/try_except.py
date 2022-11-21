>> def f(a,b):
...     return(a*b)+(a/b)
...
>>> f(4,2)
#>>10.0
>>> f(3,0)
# 정수를 0으로 나누는 오류 발생
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 2, in f
#ZeroDivisionError: division by zero


>>> def f(a,b):
...     if a and b:     # a와 b가 둘 다 0이 아닐 때
...             return (a*b) + (a/b)
...     elif a:         # a만 0이 아닐 때
...             return '불능'
...     else:           # 둘 다 0일 때
...             return '부정'
...
>>> f(3,0)
#>>'불능'
>>> f(0,3)
#>>'부정'