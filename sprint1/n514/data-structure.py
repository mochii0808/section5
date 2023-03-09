# 초기값 지정

def remainder(num, div):
    return num % div

remainder(20, 7)
'''
6
'''

# 변수명, 값 모두 전달
remainder(num=20, div=7)
'''
6
'''

# 함수에 초기값 할당
def remainder(num=20, div=7):
    return num % div

remainder()
'''
6
'''

#------------------------------------------------------------------


# 문자열 뒤집기

def reverse_string(strtest):
    left, right = 0, len(strtest) - 1
    while left < right:
        strtest[left], strtest[right] = strtest[right], strtest[left] # 변수 교환
        left += 1
        right -= 1
        
    return strtest

strtest = ['a', 'b', 'c', 'd', 'e', 'f']

print(reverse_string(strtest))

'''
['f', 'e', 'd', 'c', 'b', 'a']
'''

#=====================================

# 문자열 뒤집기 2

strtest = ['a', 'b', 'c', 'd', 'e', 'f']
strtest.reverse()
strtest

'''
['f', 'e', 'd', 'c', 'b', 'a']
'''