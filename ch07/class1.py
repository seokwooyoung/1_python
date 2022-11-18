class Person:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2

    def eat(self):
        print('냠냠~')

    def sleep(self):
        print('쿨쿨~')
    
    def talk(self):
        print('주절주절~')

class Student(Person):
    def study(self):
        print('열공!')

############################

lee = Person()
print(lee.mouth)
#>> 1

lee.talk()
#>> 주절주절~


kim = Student()
print(kim.mouth)
#>> 1

kim.study()
#>> 열공!