# 캡슐화


# class 선언
class encap:
    def __init__(self, value):
        self.value = value
        print('init :', self.value)
        
    def _set(self):
        print('set :', self.value)
        
    def printtest(self):
        print('printTest :', self.value)


# object 생성
e = encap(10)

'''
init : 10
'''

# object 실행
e.__init__(20) # 객체 value 변경
e._set()
e.printtest()

'''
init :  20
set :  20
printTest :  20
'''

#------------------------------------------------------------------


# 상속
# 같은 종류의 관계일 때 사용 (is-a)


class person:
    def __init__(self, name):
        self.name = name
        
class student(person): # person 클래스 상속
    def study(self):
        print(self.name + ' studies hard')
            # person의 상속 name
        
class employee(person): # person 상속
    def work(self):
        print(self.name + ' works hard')


# 객체 생성
s = student('Dave')
e = employee('David')

s.study()
e.work()

'''
Dave studies hard
David works hard
'''

#------------------------------------------------------------------


# 메서드 오버라이딩
# 자식 클래스에서 메소드 다시 정의

class parent():
    def exclaim(self):
        print('parent')

class child(parent):
    def exclaim(self): # 부모의 exclaim 무시
        print('child')

# 객체 생성
par = parent()
chi = child()

par.exclaim()
chi.exclaim() 

'''
parent
child
'''

#============================================

# super
# 오버라이딩시 부모의 메서드 유지

class parent():
    def exclaim(self):
        print('parent')

class child(parent):
    def exclaim(self): 
        super().exclaim() # 부모의 exclaim 메서드 유지
        print('child')

# 객체 생성
par = parent()
chi = child()

chi.exclaim() 

'''
parent 
child
'''

#------------------------------------------------------------------


# 포함
# 다른 종류의 관계일 때 (has-a)
# 속성에 인스턴스 넣어서 관리


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printperson(self, name, age):
        print('person_printperson', name, age)
    

class student:
    def __init__(self, name, age, id):
        self.person = person(name, age) # person의 인스턴스 생성
        person.__init__(self, name, age) # person의 name, age 포함
        self.id = id
        
            
# 객체 생성
s = student('Dave', 20, 1) 

# 객체 실행
print(s.name)
print(s.age)
print(s.id)

'''
Dave
20
1
'''

#------------------------------------------------------------------


# 추상화
# 미구현 추상메서드를 가지며 자식클래스에서 해당 메서드를 반드시 구현


# abc모듈 호출
from abc import *

# 추상 클래스
class people(metaclass=ABCMeta):
    @abstractmethod # 추상 메서드 선언
    def character(self):
        pass


# 상속받는 클래스
class student(people):
    def chracter(self, pow, int): # 추상 메서드 구현 (필수)
        self.pow = pow
        self.int = int

        print(f'power : {self.pow}')
        print(f'intel : {self.int}')    

# 객체 생성
s = student()

# 객체 실행
s.character(10, 100)

'''
power : 10
intel : 100
'''

#------------------------------------------------------------------


# 다형성
# 메서드명을 동일하게 하여 같은 모양의 코드가 다른 동작을 하도록

class salesworker:
    def __init__(self, name):
        self.name = name
    
    def work(self):  # 같은 이름의 메서드
        print(self.name, 'sells something') 

class devworker:
    def __init__(self, name):
        self.name = name

    def work(self):  # 같은 이름의 메서드
        print(self.name, 'develops something')


worker1 = salesworker('Dave')
worker2 = devworker('David')

worker1.work()
worker2.work()

'''
Dave sells something
Aiden develops something
'''

#============================================


# 다형성 2

class Elf:
    def __init__(self, name):
        self.name = name 
        
    def attack(self):
        print ("마법으로 공격합니다.")

class Fighter:
    def __init__(self, name):
        self.name = name 

    def attack(self):
        print ("주먹으로 공격합니다.")

elf = Elf('Dave')
fighter = Fighter('Anthony')

elf.attack()
fighter.attack()

'''
마법으로 공격합니다.
주먹으로 공격합니다.
'''
