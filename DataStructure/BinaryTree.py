from typing import List, TypeVar, Iterable
T = TypeVar('T')


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BinaryTree():
    def __init__(self):
        self.root = None

#----------------------二叉树的建立-----------------------#

    def build(self, vals: Iterable, type: str = 'bt') -> T:
        '''
        从一个数字列表建立一颗二叉树，完全二叉树by default
        '''
        if len(vals) == 0:
            return
        if type == 'bt':
            for val in vals:
                self.insert_cbt(val)
        elif type == 'bst':
            for val in vals:
                self.insert_bst(val)
        else:
            raise ValueError()
        return self

    def insert_cbt(self, val: T):
        '''
        插入一个节点到完全二叉树 (complete binary tree)
        因为是完全二叉树，所以通过BFS找到插入点
        '''
        node = TreeNode(val)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        while len(queue) != 0:
            curr_node = queue.pop(0)
            if curr_node.left != None:
                queue.append(curr_node.left)
            else:
                curr_node.left = node
                return
            if curr_node.right != None:
                queue.append(curr_node.right)
            else:
                curr_node.right = node
                return
    
    def insert_bst(self, val: T):
        '''
        插入一个节点到二叉搜索树 (binary search tree)
        
        '''

#----------------------二叉树的遍历-----------------------#

    def preorder(self, root: TreeNode):
        if root == None:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self, root: TreeNode):
        if root == None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def postorder(self, root: TreeNode):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)
  
    def BFS(self, root: TreeNode) -> List:
        '''
        非递归遍历，同样深度优先搜索也可以写成非递归形式，将队列换成栈
        '''
        vals = []
        queue = [root]
        while len(queue) != 0:
            curr_node = queue.pop(0)
            vals.append(curr_node.val)
            if curr_node.left != None:
                queue.append(curr_node.left)
            if curr_node.right != None:
                queue.append(curr_node.right)
        return vals

    def traversal(self, mode='inorder'):
        root = self.root
        if mode == 'preorder':
            self.preorder(root)
        if mode == 'inorder':
            self.inorder(root)
        if mode == 'postorder':
            self.postorder(root)

#----------------------二叉树的一些属性-----------------------#

    def get_height(self, root: TreeNode) -> int:
        '''
        求得二叉树的深度
        当节点为空时深度是0，最终返回 max(h(left), h(right)) + 1
        对于完全二叉树 h = 1 + [log2k]_ 向下取整 
        '''
        if root == None:
            return 0
        n_left = self.get_height(root.left)
        n_right = self.get_height(root.right)
        if n_left >= n_right:
            return n_left + 1
        return n_right + 1

    @property
    def height(self) -> int:
        root = self.root
        return self.get_height(root)

    @property
    def vals(self) -> List:
        root = self.root
        return self.BFS(root)

    @property
    def node_count(self) -> int:
        return len(self.vals)
    
#----------------------其他操作-----------------------#

    def mirror(self, root: TreeNode) -> TreeNode:
        '''
        镜像翻转二叉树
        '''
        if root == None:
            return 
        temp = root.left # 拷贝一下
        root.left = self.mirror(root.right) # 左子树替换为镜像之后的右子树
        root.right = self.mirror(temp) # 右子树替换为镜像之后的左子树
        return root

    def compare(self, A: TreeNode, B: TreeNode) -> bool:
        '''
        比较两颗二叉树是否相等
        '''
        if A == None and B == None:
            return True
        elif A != None and B != None:
            return A.val == B.val & self.compare(A.left, B.left) & self.compare(A.right, B.right)
        else:
            return False

    def is_subtree(self, A: TreeNode, B: TreeNode) -> bool:
        '''
        判断B是否是A的subtree，注意这里的subtree不是严格意义上的子树
        可以是叶子节点到根节点之间的任意一部分
        '''
        def traversal



if __name__ == '__main__':
    t = BinaryTree().build([1,2,3,4,5,6,7])
    t.insert(6)
    print(t.vals)
