class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)
    

  def delete(self):
    if self.get_size() > 0:
      popped = self.storage.pop(0)
      self._sift_down(0)
      for i in range(1,len(self.storage)-1):
        self._sift_down(i)
      return popped

  def get_max(self):
    return self.storage[0]


  def get_size(self):
    return len(self.storage)
  

  def _bubble_up(self, index):
    while index > 0:
      parent = (index-1)//2
      if self.storage[index] > self.storage[parent]:
        self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
        index = parent
      else:
        break
  

  def _sift_down(self, index):
    while index < (len(self.storage)-1):
      child_left = 2*index + 1 
      child_right = 2*index + 2
      if child_left <= (len(self.storage)-1) and child_right <= (len(self.storage)-1):
        if self.storage[child_left] > self.storage[child_right]:
          if self.storage[child_left] > self.storage[index]:
            self.storage[child_left], self.storage[index] = self.storage[index], self.storage[child_left]
            index = child_left
          else:
            break
        if self.storage[child_left] < self.storage[child_right]:
          if self.storage[child_right] > self.storage[index]:
            self.storage[child_right], self.storage[index] = self.storage[index], self.storage[child_right]
            index = child_right 
          else:
            break
      else:
        break

