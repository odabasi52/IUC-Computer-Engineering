class Node:
    def __init__(self, data, file):
      self.left = None
      self.right = None
      self.data = data
      self.file = file

    def insert(self, data, file):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, file)
                else:
                    self.left.insert(data, file)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, file)
                else:
                    self.right.insert(data, file)
            else:
                self.data = data

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(f"{root.data} - {root.file}")
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
  
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(f"{root.data} - {root.file}")
            res = res + self.inorderTraversal(root.right)
        return res
    
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(f"{root.data} - {root.file}")
        return res
    
    def search(self, root, data):
        if root is None or root.data == data:
            return root
        if root.data < data:
            return self.search(root.right, data)
        return self.search(root.left, data)
