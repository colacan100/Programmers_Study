# 클래스에 연결리스트 구현
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class linked_list:
  def __init__(self, value):
    self.head = Node(value)

  def add_node(self, value):
    if self.head == None:
      self.head = Node(value)
    else:
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(value) # init함수의 value

  # 연결리스트의 삭제구현
  def del_node(self,value):
    if self.head == None:
      # 해당 값에 대한 노드는 없다.
      # 의미없는 조건에서 함수는 아무것도 반환하지 않는다. 
    elif self.head.value == value:
      # 노드의 위치를 변경시킨다.
      # 변경된 노드에 대해서 삭제를 진행한다.
    else:
      node = self.head
      while node.next:
        if node.next.value == value:
         # 노드의 위치를 변경시킨다.
         # 변경된 노드에 대해서 삭제를 진행한다.
        else : 
         # 다음 노드의 위치를 현재 노드에 넣어준다.

  # 연결리스트의 노드출력을 위한 기능
  def ord_desc(self):
    node = self.head
    while node:
      print(node.value)
      node = node.next 

# 노드출력 테스트
linkedlist = linked_list(0)
linkedlist.ord_desc()

# 노드 삽입 테스트
for value in range(1,10):
  linkedlist.add_node(value)
linkedlist.ord_desc()

linkedlist.head