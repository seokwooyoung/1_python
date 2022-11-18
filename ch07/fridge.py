# 코끼리를 냉장고에 넣기
# isOpened : 문이 열려있는지
# foods : 냉장고 안에 들어있는 음식들의 리스트 


class Fridge:
    def __init__(self):
        self.isOpened = False   
        self.foods = []

    # 냉장고 문을 여는 메서드
    def open(self):
        self.isOpened = True
        print('냉장고 문을 열었습니다.')

    # 냉장고 안에 음식을 넣는 메서드
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print('냉장고 안에 음식이 들어갔습니다.')
        else:
            print('냉장고 문이 닫혀있어 음식을 못 넣겠습니다.')

    # 냉장고 문을 닫는 메서드
    def close(self):
        self.isOpened = False
        print('냉장고 문을 닫았습니다.')

class Food:
    pass

######################################################################

import fridge

f = fridge.Fridge()
apple = fridge.Food()
elephant = fridge.Food()

f.open()
#>> 냉장고 문을 열었습니다. 

f.put(apple)
#>> 냉장고 안에 음식이 들어갔습니다.

f.put(banana)
#>> Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'banana' is not defined

f.put(elephant)
#>> 냉장고 안에 음식이 들어갔습니다.

f.put(lion)
#>> Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'lion' is not defined

f.foods
#>> [<fridge.Food object at 0x00000215A880A5C0>, <fridge.Food object at 0x00000215A87C4A30>]