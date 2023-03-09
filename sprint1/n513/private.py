# private

class point:
    def __init__(self):
        # private 변수 선언
        self.__private_name = 'private 접근'

class point_sub(point): # 상속
    def __init__(self):
        point.__init__(self)


# 객체 생성
my_point = point()
my_point_sub = point_sub()

# private 접근 (불가)
print(my_point.__private_name)

'''
AttributeError: 'point' object has no attribute '__private_name'
'''

# private 접근 (가능)
# _클래스명__메소드명
print(my_point._point__private_name)
print(my_point_sub._point__private_name)


'''
private 접근
private 접근
'''

#-------------------------------------------------------------------


# 속성 충돌

class parent_class:
    def __init__(self):
        self.__value = 50

class sub_class(parent_class):
    def __init__(self):
        super().__init__() # 부모 클래스의 init 호출
        self.__value = 60 # __value 충돌

# 객체 생성
s = sub_class()

# 같은 속성명 __value 충돌
print(s._parent_class__value)
print(s._sub_class__value)

'''
50
60
'''

