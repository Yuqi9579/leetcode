class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, vals):
        self.root = self._build(vals)

    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val <= root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def traversal(self, type='inorder'):
        if type == 'preorder':
            self._preorder(self.root)
        if type == 'inorder':
            self._inorder(self.root)
        if type == 'postorder':
            self._postorder(self.root)
        return self

    def _build(self, vals):
        root = None
        for val in vals:
            root = self.insert(root, val)
        return root

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        print(root.val)
        self._inorder(root.right)

    def _preorder(self, root):
        if not root:
            return
        print(root.val)
        self._preorder(root.left)
        self._preorder(root.right)

    def _postorder(self, root):
        if not root:
            return
        self._postorder(self.root)
        self._postorder(self.root)
        print(root.val)

if __name__ == '__main__':
    bst = BinarySearchTree([2,5,4,3,4,7,8,3,5,3,9,8,9,4])
    bst.traversal(type='inorder')

    