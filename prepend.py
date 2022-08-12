from main import Node, LinkedList

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

my_linked_list = LinkedList(23)
my_linked_list.append(45)
my_linked_list.prepend(234)
my_linked_list.print_list()  
  
  