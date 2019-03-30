class BinaryTree():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)

        print(root.data,end=" ")

        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")


def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
inorder(root)
print()
print()
postorder(root)
print()
print()
preorder(root)