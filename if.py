
""" 
# 10 보다 큰 수 입력하면 알려주기.
num = int(input('정수 : '))
if num <= 10:
    print(num)
else:
    print(num,'is too big')
"""

# 10 보다 큰 수 입력하면 알려주고 나가기. 
while True:
    num = int(input('정수 : '))
    if num <= 10:
        print(num)
    else:
        print(num, 'is too big')
        break

