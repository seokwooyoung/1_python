# 회문 : 거꾸로 배열해도 같은 단어 혹은 문장이 되는 것 ex)anna, level
# 주어진 단어가 회문인지 판별하는 함수 palindrom()

def palindrom(text):
    text = str(input('단어를 입력하시오.:'))
    a = text.lower()        # 소문자로
    b = a.replace(" ", "")  # 공백 제거
    if b[:] == b[::-1]:
        print('True')
    else:
        print('False')

palindrom(any)