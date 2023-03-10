# 큐

# deque로 구현

from collections import deque

queue = deque(['Eric', 'John', 'Michael'])

queue.append('Terry') # 뒤에 추가
queue.append('Graham') # 뒤에 추가

print(queue)

'''
deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
'''

queue.popleft() # 왼쪽에서 제거 (Eric)
queue.pop() # 오른쪽에서 제거 (Graham)

print(queue)

'''
deque(['John', 'Michael', 'Terry'])
'''

#============================================

# 연결리스트로 큐 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 큐 클래스
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    # 큐에 값넣기
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None: # 큐가 비었다면
            self.front = new_node
            self.rear = new_node
        else: # 큐가 있다면
            self.rear.next = new_node # 새로운 최종 노드 생성
            self.rear = new_node # 최종 노드에 삽입
        return new_node.data
    
    # 큐에서 값 빼기 (FIFO)
    def dequeue(self):
        if self.front is not None: # 큐에 값이 있다면
            old_front = self.front
            self.front = old_front.next # 기존 front를 다음 값으로 교체 (맨 앞 데이터 제거)
        
        if self.front is None:
            self.rear = None
            
        return old_front.data
    
    # 리스트 출력
    def ord_desc(self):
        node = self.front
        while node:
            print(node.data)
            node = node.next

# 큐 생성
q = Queue()

# 삽입
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(2)

q.ord_desc()

'''
1
2
3
2
'''

# 제거
q.dequeue() # 맨 앞에서 제거

q.ord_desc()

'''
2
3
2
'''

#--------------------------------------------------------------------------

 # 스택

 # 리스트로 스택 구현

stack = [3,4,5]
stack.append(6)
stack.append(7)

print(stack)

'''
[3, 4, 5, 6, 7]
'''

stack.pop() # 7
stack.pop() # 6
stack.pop() # 5

print(stack)

'''
[3, 4]
'''

#========================

# 클래스로 구현

class Stack:
    def __init__(self):
        self.data = []
    
    # 삽입
    def push(self, item):
        self.data.append(item)

    # 제거
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return 'Empty'
    
#=========================

# 연결리스트로 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    # 삽입
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top 
        self.top = new_node
        return new_node.data
    
    # 제거
    def pop(self):
        popped_node = self.top
        self.top = popped_node.next
        return popped_node.data

    # 출력  
    def ord_desc(self):
        node = self.top
        while node:
            print(node.data)
            node = node.next

# 스택 생성
s = Stack()

# 삽입
s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.ord_desc()

'''
4
3
2
1
'''

# 제거
s.pop()
s.pop()

s.ord_desc()

'''
2
1
'''