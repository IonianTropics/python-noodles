
class BinTree:

    def __init__(self, right, left):
        self.right = right
        self.left = left


def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root


x = BinTree(BinTree(1, 2), BinTree(3, 4))

y = invertTree(x)

assert x.right.right == y.left.left
