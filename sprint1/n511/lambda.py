# 인라인(한 줄) 코딩

a = 5
b = 1 if a==2 else (2 if a>3 else 3)
print(b)


'''
2
'''

#------------------------------------------------------------------------------------------


# lambda

define_word = lambda word1, define : word1*define # 함수 정의

result = define_word('abc|', 4) # 함수 호출

print(result)


'''
abc|abc|abc|abc|
'''

#------------------------------------------------------------------------------------------


# map

spelling = ['test1', 'test2', 'test3']

spells = map(lambda item : item + '!!!', spelling)

spells_list = list(spells) # map은 생성자이므로 list로 제작

print(list(spells_list))


'''
['test1!!!', 'test2!!!', 'test3!!!', 'test4!!!']
'''

#------------------------------------------------------------------------------------------


# filter

fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

result = filter(lambda member : len(member) > 6, fellowship) # 조건에 맞으면 lambda 적용

result_list = list(result) # filter도 생성자

print(result_list)


'''
['samwise', 'aragorn', 'boromir', 'legolas', 'gandalf']
'''

#------------------------------------------------------------------------------------------


# reduce
# 집계 함수

from functools import reduce

stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

result = reduce(lambda item1, item2 : item1 + item2, stark) # 누적합 연산

print(result)


'''
robbsansaaryabrandonrickon
'''