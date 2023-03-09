# OOP, 객체 지향 프로그래밍

class bus:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive_bus(self):
        self.speed = 70

class car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive_car(self):
        self.speed = 50


# 객체 생성(정지 중)
my_car = car(0, 'green', 'test-model')
my_bus = bus(0, 'black')
print(my_car.speed)
print(my_bus.speed)

'''
0
0
'''

# 객체 실행(운전 중)
my_car.drive_car()
my_bus.drive_bus()
print(my_car.speed)
print(my_bus.speed)

'''
50
70
'''