# comprehension
# -> 리스트 한줄 작성

# 기본
[n for n in range(10)]


'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

#-----------------------------------------------------------------------


# 리스트에 대한 comprehension

nums = [1, 2, 3, 4, 5]

[n**2 for n in nums]


'''
[1, 4, 9, 16, 25]
'''

#-----------------------------------------------------------------------


# for문과 if문의 comprehension

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

[a for a in list_a for b in list_b if a == b]


'''
[2, 3, 4]
'''


### 동일 for 문
'''
common_num = []

for a in list_a:
    for b in list_b:
        if a == b:
            common_num.append(a)
'''

#-----------------------------------------------------------------------


# dictionary comprehension

dic = {'A':0, 'B':0, 'C':1, 'D':0, 'E':1}

{key:val for key, val in dic.items() if val == 1}


'''
{'C': 1, 'E': 1}
'''