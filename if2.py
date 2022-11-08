# k 단위기호 표기
# M 단위기호 표기

num = int(input('입력 : '))
result = str(num)

if 1000000 <= num:
    result = str(num // 1000000) + 'M'
elif 1000000 >= num >= 1000:
    result = str(num // 1000) + 'k'
elif num < 1000:
    pass

print(result)