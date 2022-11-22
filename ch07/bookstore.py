# __init__ 메소드 (초기화)

class Book:
    def setData(self, title, price, author):
        self.title=title
        self.price=price
        self.author=author

    def printData(self):
        print('제목 : ', self.title)
        print('가격 : ', self.price)
        print('저자 : ', self.author)

    #1. 초기화 메소드
#    def __init__(self):
#        print('책 객체를 새로 만들었어요.')

    #2. 초기화 메소드 (클래스의 객체가 만들어질 때 자동으로 호출되어 그 객체가 갖게 될 여러가지 성질을 정해줌)
    def __init__(self, title, price, author):
        self.setData(title, price, author)
        print('책 객체를 새로 만들었어요.')

#################################################################
"""
1. 실행
import bookstore
b = bookstore.Book()
#>> 책 객체를 새로 만들었어요.

b.setData('누가 내 치즈를 먹었을까', '300원', '미키')
b.printData()
# 제목 :  누가 내 치즈를 먹었을까
# 가격 :  300원
# 저자 :  미키
"""

"""
2. 실행
import bookstore
b = bookstore.Book('누가 내 치즈를 먹었을까','300원','미키')
#>> 책 객체를 새로 만들었어요.

b.printData()
# 제목 :  누가 내 치즈를 먹었을까
# 가격 :  300원
# 저자 :  미키

"""