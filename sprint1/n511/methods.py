# rjust, ljust
# 문자열 앞,뒤 채우기

print('2'.rjust(4, '1'))
print('2'.ljust(4, '1'))
print('50000'.rjust(5, '1'))
print("50000".rjust(9, '1'))


'''
1112
2111
50000
111150000
'''

#------------------------------------------------------------------------------------------


# zfill
# 앞부분 0으로 채우기

print('2'.zfill(3))


'''
002
'''

#------------------------------------------------------------------------------------------

string_ = "Hello, I am Jack and I am a data scientist"


# split

string_.split(' ')

'''
['Hello,', 'I', 'am', 'Jack', 'and', 'I', 'am', 'a', 'data', 'scientist']
'''


# startswith

string_.startswith('Hello')

'''
True
'''


# endswith

string_.endswith('scientist')

'''
True
'''


# replace

string_.replace('Jack', 'John')

'''
Hello, I am John and I am a data scientist
'''

#------------------------------------------------------------------------------------------


# copy, 얕은 복사

import copy

a = {'a':5, 'b':4, 'c':6}

a_a = a # 선언하여 copy하면 데이터 변경 연동
a_copy = a.copy() # copy 데이터에서 삭제시 copy 데이터만 삭제
a_copy_copy = copy.copy(a)

del a_a['a'] 

print(a)
print(a_a)
print(a_copy) 
print(a_copy_copy)


'''
{'b': 4, 'c': 6}
{'b': 4, 'c': 6}
{'a': 5, 'b': 4, 'c': 6}
{'a': 5, 'b': 4, 'c': 6}
'''

#------------------------------------------------------------------------------------------


# deep copy, 깊은 복사
# 완전히 새로운 변수 생성

import copy

list_var = [[1,2], [3,4]]
list_var_copy = list_var.copy()
list_var_deepcopy = copy.deepcopy(list_var)


list_var[1].append(5)

print(list_var)
print(list_var_copy)
print(list_var_deepcopy)



'''
[[1, 2], [3, 4, 5]]
[[1, 2], [3, 4, 5]]
[[1, 2], [3, 4]]
'''