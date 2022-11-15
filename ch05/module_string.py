"""
import string

# 대문자 A~Z
string.ascii_uppercase
#>> 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 소문자 a~z
string.ascii_lowercase
#>> 'abcdefghijklmnopqrstuvwxyz'

# 소문자 & 대문자
string.ascii_letters
#>> 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 숫자
string.digits
#>> '0123456789'

alphanum = string.ascii_letters + string.digits
print(alphanum)
#>> abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
len(alphanum)
#>> 62
"""
# string+random 비밀번호 만들기
import string
import random

password = str()

# 영어 대문자, 소문자, 숫자, 특수문자(!, ~)
for i in range(10):
    alphanum = list(set(string.ascii_letters+string.digits))+['!~']
    password = password + random.choice(alphanum)

print(password)
