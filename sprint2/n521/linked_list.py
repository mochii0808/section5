# 연결 리스트

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class linked_list:
    def __init__(self, value):
        self.head = Node(value)

    def add_node(value):
        node = head
        while node.next: # 헤드 노드 뒤에 노드가 있다면
            node = node.next # 다음 노드로 node 지정

        # 새로 만든 최종 노드위치에 새로운 노드 생성
        node.next = Node(value)


# 헤드 노드 생성
head = Node(5)

# 연결 리스트에 노드 추가
linked_list.add_node(11) # 5 - 11
linked_list.add_node(17) # 5 - 11 - 17

print(head.value)
print(head.next.value)
print(head.next.next.value)

'''
5
11
17
'''

#=====================================


# 노드 연결

node1 = Node(3)
node2 = Node(4)
node3 = Node(5)
node4 = Node(6)

# 참조
node1.next = node2
node2.next = node3
node3.next = node4

# 헤드노드 지정
node = node1

# 노드 출력
while node: # 노드에 값이 있다면(None이 아니라면)
    print('value :', node.value)
    node = node.next # 현재 노드 변경

'''
value : 3
value : 4
value : 5
value : 6
'''

#-----------------------------------------------------------------------


# 삭제, 조회, 출력 기능

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class linked_list:
    def __init__(self, value):
        self.head = Node(value)
    
    # 삽입
    def add_node(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)

    # 삭제  
    def del_node(self, value):
        if self.head == None: # 헤드가 없을 경우
            print('None')
            
        elif self.head.value == value: # 헤드값일 경우
            self.head = self.head.next # 헤드값 삭제

        else: 
            node = self.head
            while node.next: # 다음 노드가 있을경우
                if node.next.value == value: # 해당 노드일 경우
                    node.next = node.next.next # 해당 노드 삭제
                else: 
                    node = node.next # 다음 노드로

    # 조회
    def search_node(self, value):
        node = self.head
        while node.next:
            if node.value == value:
                return node
            else:
                node = node.next

    # 전체 출력       
    def ord_desc(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


# 노드 삽입
linkedlist = linked_list(0)
for value in range(1, 10):
    linkedlist.add_node(value)
linkedlist.ord_desc()

'''
0
1
2
3
4
5
6
7
8
9
'''

# 노드 삭제
linkedlist.del_node(5)
linkedlist.del_node(3)

linkedlist.ord_desc()

'''
0
1
2
4
6
7
8
9
'''