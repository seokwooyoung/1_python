# 입력한 정수까지의 제곱수 출력

num = int(input('정수를 입력하시오. : '))

for i in range(1, num+1):
    j = i * i
    print(i, j)