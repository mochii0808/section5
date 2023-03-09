# constant time
# 데이터 크기와 상관없는 소요 시간

items = [1, 2, 3]

print(items[0])

'''
1
'''

#------------------------------------------------------------------


# linear time
# 데이터 크기에 선형 비례

for item in items:
    print(item)

'''
1
2
3
'''

#------------------------------------------------------------------


# quadratic time
# 데이터 크기의 제곱에 비례


for item1 in items:
    for item2 in items:
        print(item1, item2)

'''
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
'''

#------------------------------------------------------------------


# worst case
# 경우에 따라 소요 시간이 달라짐

def search_thing(items, thing):
    for item in items: # 반복문 -> O(n)
        if item == thing:
            return True
        
    return False

search_thing([1, 2, 3], 4)

# 최종 경우인 False 출력 -> 선형 시간
'''
False
'''
#------------------------------------------------------------------


# log time
# 입력값의 증가율과 출력값의 증가율이 동일하지 않음

def test(n):
    cnt = 0
    i = 1
    while i < n:
        i *= 2
        cnt += 1
    return cnt

test(10)
'''
4
'''

test(100)
'''
7
'''