"""
# pickle module : 복잡한 자료를 파일에 쓰고 읽기

# 회원의 ID와 비밀번호를 파일에 저장
users = {'kim':'123dne', 'lee':'907udde', 'park':'j39hg09'}
f = open('users', 'wb') # wb : 바이트 형식으로 쓰겠다. 

import pickle
pickle.dump(users,f)
f.close()

# 확인
import os
os.path.exists('users')

# 읽어보기
f = open('users','rb')
a = pickle.load(f)
print(a)
"""

###################################################################
# glob module : 파일들의 리스트를 뽑을 때 사용

from glob import glob
glob('*.txt')
#>> ['hello.txt','ko_en.txt','letter.txt','postcard.txt']

###################################################################
# os.path

from glob import glob
from os.path import isdir

for x in glob('*'):
    if isdir('*'):      # 리스트의 원소가 디렉토리면,
        print(x, '<DIR>')    
    else:
        print(x)
