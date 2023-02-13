# for

data = [90, 45, 32, 44]
for i in range(len(data)):
    print(data[i])


'''
90
45
32
44
'''

#------------------------------------------------------------------------------------------


# dict 출력 

mock_data = {
  "id": 1,
  "first_name": "states",
  "last_name": "code",
  "email": "code@states.com",
  "gender": "Female",
  "ip_address": "123.123.123.23"
}

for x in mock_data: # key 출력
    print(x)

print('-'*20)

for x in mock_data.values(): # value 출력
    print(x)

print('-'*20)

for x in mock_data.items(): # item tuple 출력
    print(x)

print('-'*20)

for k, v in mock_data.items(): # key, value 함께 출력
    print(k, v)


'''
id
first_name
last_name
email
gender
ip_address
--------------------
1
states
code
code@states.com
Female
123.123.123.23
--------------------
('id', 1)
('first_name', 'states')
('last_name', 'code')
('email', 'code@states.com')
('gender', 'Female')
('ip_address', '123.123.123.23')
--------------------
id 1
first_name states
last_name code
email code@states.com
gender Female
ip_address 123.123.123.23
'''

#------------------------------------------------------------------------------------------


# break

int_list = [0,1,2,3,4,5,6,7]

for x in int_list:
    if x==3:
        break # 탈출
    else:
        print(x)


'''
0
1
2
'''


# continue

for x in int_list:
    if x ==3:
        continue # 현재 루프 생략
    else:
        print(x)


'''
0
1
2
4
5
6
7
'''
