from main import Node, LinkedList

def get(self, index):
  if index < 0 or index >= self.length:
    return None
  temp = self.head
  for _ in range(index):
      temp = temp.next

  return temp

my_linked_list = LinkedList(12)
my_linked_list.append(25)
my_linked_list.append(51)

print(my_linked_list.get(2))

  
    
      
