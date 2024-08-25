class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        self.head = None
        self.tail = None
        
        self.length = 0
        
    # Insertion Method
    def append(self, data):
        new_node = Node(data)
        self.tail = new_node
        self.tail.next = new_node
        self.length += 1



if __name__ == "__main__":
  l = LinkedList()
  l.append(10)
  l.append(20)
  l.append(30)
  l.append(40)
  l.append(50)
  l.append(15)

  l.head.data
  l.head.next.data
  l.head.next.next.data
