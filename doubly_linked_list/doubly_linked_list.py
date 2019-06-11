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
    holder = self.head
    self.head = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return holder.value

  def add_to_tail(self, value):
    new_node = ListNode(value, None, None)
    self.length += 1
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def remove_from_tail(self):
    holder = self.tail
    self.tail = None
    self.length -= 1
    if self.length == 0:
      self.head = None
    return holder.value

  def move_to_front(self, node):
    holder = self.head
    holder.prev = self.head
    self.head = node
    self.head.insert_after(holder.value)
    node.delete()

  def move_to_end(self, node):
    holder = self.tail
    holder.next = self.tail
    self.tail = node
    self.tail.insert_before(holder.value)
    node.delete()

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
