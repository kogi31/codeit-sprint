class Node:
    def __init__(self, data):
        self.data = data # 노드가 작성하는 값
        self.next = None # 다음 노드를 가리키는 포인터


# 링크드 리스트 클래스 정의
class LinkedList:
    def __init__(self):
        self.head = None # 링크드 리스트의 시작 노드(헤드)

        
    # 리스트의 끝에 새로운 노드 추가하는 함수
    def append(self, data):
        new_node = Node(data) # 새 노드 생성
        if self.head is None: # 조건
            self.head = new_node # 새로운 노드를 헤드로 설정
            return
        
        # 리스트의 마지막 노드 찾기
        last = self.head
        while last.next:
            last = last.next

        # 마지막 노드의 next를 새 노드로 설정
        last.next = new_node
    
        # 리스트의 맨 앞에 새로운 노드를 추가하는 함수
    def prepend(self, data):
        new_node = Node(data)  # 새 노드를 생성
        new_node.next = self.head  # 새 노드의 next를 현재 헤드로 설정
        self.head = new_node  # 헤드를 새 노드로 변경

    def delete(self, key):
        # 헤드가 삭제할 노드를 가리킬 경우
        current = self.head
        if current is not None:
            if current.data == key:
                self.head = current.next # 헤드를 다음 노드로 변경
                current = None # 현재 노드를 삭제
                return
        
        # 삭제할 노드 찾기
        prev = None
        while current is not None:
            if current.data == key: # 삭제하려는 값 발견
                break
            prev = current
            current = current.next

        if current is None:
            return
        
        prev.next = current.next
        current = None

    def delete_head(self):
        if self.head is None:
            return
        
        self.head = self.head.next
        
    # 리스트의 모든 요소를 출력하는 함수
    def display(self):
        current = self.head # 헤드부터 시작
        while current:
            print(current.data)
            current = current.next # 다음 노드로 이동

    

l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(15)

l.prepend(1)

l.delete(15)
l.delete(40)
l.delete(50)

l.delete_head()
l.display()


