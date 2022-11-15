# 피타고라스의 정리 
# 두 직각변(a,b)의 길이를 입력으로 받아 빗변(c)의 길이를 구하는 함수 hypotenuse()를 작성
# 소수점 셋째 자리에서 반올림
import math

def hypotenuse(a, b):
    c1 = a**2 + b**2
    c2 = c1**(1/2)
    c3 = round(c2,3)
    print(c3)

hypotenuse(2,4)