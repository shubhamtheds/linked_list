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



  
  
      

  
      
    
    
  
    