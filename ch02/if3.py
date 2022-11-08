# 입력받은 정수의 합 (음수가 입력되면 중단)

result = 0
while True:
    num = int(input())
    if num >= 0:
        result = result + num
    elif num < 0:
        break
print('총 합:',result)
