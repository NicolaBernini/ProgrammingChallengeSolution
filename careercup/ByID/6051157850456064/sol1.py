
# BST

class Node:
  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def insert(self, val):
    if self.val == None:
      self.val = val
    elif val <= self.val:
      if self.left == None:
        self.left = Node(val=val)
      else:
        self.left.insert(val)
    else:
      if self.right == None:
        self.right = Node(val=val)
      else:
        self.right.insert(val)

  def show_in_order(self, res=""):
    if self.left is not None:
      res = self.left.show_in_order(res=res)
    res += ("," if len(res) > 0 else "") + str(self.val)
    if self.right is not None:
      res = self.right.show_in_order(res=res)
    return res


  
