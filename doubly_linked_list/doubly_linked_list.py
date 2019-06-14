"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value, prev = None, next = None)
    self.length += 1
    if not self.head and not self.tail:
      self.tail = new_node
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def remove_from_head(self):
    if self.length == 0:
      return None
    if self.length == 1:
      holder = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return holder.value
    if self.length >= 2:
      next_head = self.head.next
      holder = self.head
      self.head = next_head
      self.head.prev = None
      self.length -= 1
      return holder.value

  def add_to_tail(self, value):
    new_node = ListNode(value, prev = None, next = None)
    self.length += 1
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def remove_from_tail(self):
    if self.length == 0:
      return None
    if self.length == 1:
      holder = self.tail
      self.head = None
      self.tail = None
      self.length -= 1
      return holder.value
    if self.length >= 2:
      prev_tail = self.tail.prev
      holder = self.tail
      self.tail = prev_tail
      self.tail.next = None
      self.length -= 1
      return holder.value

  def move_to_front(self, node):
    if self.length < 2 or node is self.head:
      return
    elif self.length == 2 and node is self.tail:
      self.head, self.tail = self.tail, self.head
      self.head.next = self.tail
      self.tail.prev = self.head
      self.head.prev = None
      self.tail.next = None
    else:
      prev_node = node.prev
      next_node = node.next
      prev_node.next = next_node
      next_node.prev = prev_node
      self.head.prev = node
      node.next = self.head
      node.prev = None
      self.head = node

  
  def move_to_end(self, node):
    if self.length < 2 or node is self.tail:
      return
    elif self.length == 2 and node is self.head:
      self.head, self.tail = self.tail, self.head
      self.head.next = self.tail
      self.tail.prev = self.head
      self.head.prev = None
      self.tail.next = None
    else:
      prev_node = node.prev
      next_node = node.next
      prev_node.next = next_node
      next_node.prev = prev_node
      self.tail.next = node
      node.prev = self.tail
      node.next = None
      self.tail = node

  def delete(self, node):
    if self.head is node:
      self.remove_from_head()
    elif self.tail is node:
      self.remove_from_tail()
    else:
      self.length -= 1
      node.delete()

  def get_max(self):
    if self.length == 0:
      return None
    if self.length == 1:
      return self.head.value
    else:
      temp = self.head
      max = 0
      while temp is not None:
        if temp.value > max:
          max = temp.value
        temp = temp.next
      
      return max
