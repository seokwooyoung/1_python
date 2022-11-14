# 입력받은 정수에 해당하는 한글 문자열을 반환하는 함수 korean_number() 
# if문 사용 불가
"""
def korean_number(num):
    num = int(input('정수를 입력하시오.(1~9): '))

    number = {1:'일', 2:'이', 3:'삼', 4:'사', 5:'오', 6:'육',7:'칠', 8:'팔', 9:'구'}
    print(number['num'])

korean_number(num)
"""

# resolve
def korean_number(num):
    d = {0: '영', 1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
    return d[num]

