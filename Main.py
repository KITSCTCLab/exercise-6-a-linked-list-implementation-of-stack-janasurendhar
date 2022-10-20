 class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    n = Node(data)
    if self.head == None:
        self.head = n
    else:
        n.next = self.head
        self.head = n
      

  def pop(self) -> None:
    if self.head == None:
        return
    self.head = self.head.next

  def status(self):
    """
    It prints all the elements of stack.
    """
    t = self.head
    while t!= None:
        print(t.data, end = "=>")
        t = t.next
    print(t)


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
