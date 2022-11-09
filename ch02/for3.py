# 최소 안전 온도, 최대 안전 온도
# 화학반응 완료되면 -999를 보냄
# 기록된 온도가 올바른 범위에 있는 경우 "nothing to report"
# 기록된 온도가 위험 수준에 도달 "Alert!", 온도 측정 중단

"""
# 1
L = input().split()
min_num = int(L[0])
max_num = int(L[1])

# 2
min, max = map(int, input().split())
"""

# 3
min_num = int(input('최소 안전 온도 : '))
max_num = int(input('최대 안전 온도 : '))

temp = int(input(""))

while temp != -999:
    if min_num <= temp <= max_num:
        print("Nothing to report")
        temp = int(input(""))   # 다시 측정
    else:
        print("Alert!")
        break
    