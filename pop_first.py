from main import Node LinkedList

def pop_first(self):
  if self.length == 0:
    return None
  temp = self.head
  self.head = self.head.next
  temp.head = None
  self.length -=1
  