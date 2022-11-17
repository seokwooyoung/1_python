# 1. 파일 읽기
txt = open("postcard.txt", "r").read()
print("*** 1. Full Text ***\n" + txt + '\n')

# 2. 본문 추려내기
head, body, tail = tuple(txt.split('\n\n'))
print("*** 2. Body ***\n" + body + '\n')

# 3. 문장부호 제거
import re
s = re.sub('[:,\.]', '', body)
print("*** 3. Text without Punctuation ***\n" + s + '\n')

# 4. 대문자로 변환
s = s.upper()
print("*** 4. Uppercase ***\n" + s + '\n')

# 5. 비밀 메시지 출력
secret_words = []
for line in s.split('\n'):
    secret_words += line.split()[:2]

message = ' '.join(secret_words)
print("*** 5. Secret Message ***\n" + message)