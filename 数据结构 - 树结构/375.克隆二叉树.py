"""
375. 克隆二叉树
深度复制一个二叉树。

给定一个二叉树，返回一个他的 克隆品 。

样例
给定一个二叉树：

     1
   /  \
  2    3
 / \
4   5
返回其相同结构相同数值的克隆二叉树：

     1
   /  \
  2    3
 / \
4   5
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree
    @return: root of new tree
    """

    # time:1266 ms
    def cloneTree(self, root):
        # write your code here
        if not root:
            return
        new = TreeNode(root.val)
        new.left, new.right = root.left, root.right
        self.cloneTree(root.left)
        self.cloneTree(root.right)
