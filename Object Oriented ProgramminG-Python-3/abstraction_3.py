class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insertLeft(self, key):
        if self.left == None:
            self.left = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.left = self.left
            self.left = t

    def insertRight(self, key):
        if self.right == None:
            self.right = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.right = self.right
            self.right = t

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key
bt = BinaryTree('a')
print(bt.getRootVal())
print(bt.getLeftChild())
bt.insertLeft('b')
print(bt.getLeftChild())
print(bt.getLeftChild().getRootVal())
bt.insertRight('c')
print(bt.getRightChild())
print(bt.getRightChild().getRootVal())
bt.getRightChild().setRootVal('hello')
print(bt.getRightChild().getRootVal())