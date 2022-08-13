class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length +=1
    return True

  def pop(self):  # removing the element from the last.
    if self.length == 0:
      return  None

    temp = self.head
    pre = self.head

    while (temp.next):
      pre = temp
      temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1

    if self.length == 0:
      self.head=None
      self.tail=None

    return temp.value


  def prepend(self, value): # adding element starting of the linked list.
    new_node = Node(value)
    if  self.length == 0:
      self.head = new_node
      self.tail = new_node

    else:
      new_node.next = self.head
      self.head = new_node
      self.length +=1
    return True

  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    self.head = self.head.next
    temp.head = None
    self.length -=1
    return temp
  

  def get(self, index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for _ in range(index):
      temp = temp.next

    return temp



  def set_value(self, index, value): 
       #we can't assign set as it is already is defined in Python.
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False


  def insert(self, index, value):
  
    if index < 0 or index > self.length:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)

    new_node = Node(value)
    temp = self.get(index -1)
    new_node.next = temp.next
    temp.next = new_node
    self.length +=1
    return True             

  def remove(self, index):
    if index < 0 or index > self.length:
      return None
    if index == 0:
      return self.pop_first()
    if index == self.length - 1:
      return self.pop()
    pre = self.get(index - 1)
    temp = pre.next
    pre.next = temp.next
    temp.next = None
    return temp.value


  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after


# my_linked_list = LinkedList(12)
# my_linked_list.append(23)
# my_linked_list.append(35)
# my_linked_list.append(47)
# my_linked_list.append(58)
# my_linked_list.append(73)

# my_linked_list.reverse()

# my_linked_list.print_list()

      



    
    









    











# my_linked_list = LinkedList(23)
# my_linked_list.append(35)
# my_linked_list.append(56)
# my_linked_list.append(78)


# my_linked_list.remove(2)

# my_linked_list.print_list()

    
# my_linked_list = LinkedList(0)
# my_linked_list.append(2)
# my_linked_list.append(4)
# my_linked_list.append(6)

# my_linked_list.insert(2, 56)

# my_linked_list.print_list()
# my_linked_list = LinkedList(12)
# my_linked_list.append(25)
# my_linked_list.append(51)
# my_linked_list.set_value(2, 34)

# my_linked_list.print_list()
# my_linked_list = LinkedList(12)
# my_linked_list.append(25)
# my_linked_list.append(51)

# print(my_linked_list.get(2))
# print(my_linked_list.get(3))
    
# my_linked_list1 = LinkedList(505)
# my_linked_list1.prepend(234)
# my_linked_list1.print_list()

# my_linked_list = LinkedList(23)
# my_linked_list.append(45)
# my_linked_list.prepend(234)
# my_linked_list.print_list()

# # (2) Items - Returns 2 Node
# print(my_linked_list.pop())
# # (1) Item -  Returns 1 Node
# print(my_linked_list.pop())
# # (0) Items - Returns None
# print(my_linked_list.pop())

# my_linked_list.print_list()

  
# my_linked_list = LinkedList(23)
# my_linked_list.append(45)
# my_linked_list.print_list()

# list = [45, 67, 78, 86, 45, 345, 6789, 34]
# for i in range(len(list)):
#   my_linked_list.append(list[i])
  

  
# my_linked_list.print_list()



  
  
      

  
      
    
    
  
    