# try - except

a = 10
b = 0

try:
    a/b
except:
    print('can not')

'''
can not
'''

#============================

try:
    a/b
except ZeroDivisionError: # 다른 에러는 except 처리 X
    print('can not')

'''
can not
'''

#============================

try:
    a/b
except ZeroDivisionError as e:
    print(e)

'''
division by zero
'''

#-----------------------------------------------------------------------


# try - except - else

a = 10
b = 0
c = 2

try:
    a/c
except:
    print('can not')
else:
    print('can')

'''
can
'''

#-----------------------------------------------------------------------


# try - except - finally

try:
    a/b
except:
    print('can not')
finally: # except 여부와 상관없이 항상 실행
    print('end')

'''
can not
end
'''