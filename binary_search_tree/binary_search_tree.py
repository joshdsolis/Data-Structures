class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self.value > value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif self.value < value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    elif self.left.value and self.right.value:
      if self.left.value == target:
        return True
      elif self.right.value == target:
        return True
    elif self.value < target:
      if self.right.value:
        self.right.contains(target)
    elif self.value > target:
      if self.left.value:
        self.left.contains(target)
    else:
      return False

  def get_max(self):
    if self.right:
      max = self.right.get_max()
    else:
      return self.value
    return max


  def for_each(self, cb):
    if self.right and self.left:
      cb(self.right)
      cb(self.left)
      self.for_each(cb)
    elif self.right and not self.left:
      cb(self.right)
      self.for_each(cb)
    elif self.left and not self.right:
      cb(self.left)
      self.for_each(cb)
    else:
      pass