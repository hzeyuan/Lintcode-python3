"""
245. 子树
有两个不同大小的二叉树： T1 有上百万的节点； T2 有好几百的节点。请设计一种算法，判定 T2 是否为 T1的子树。

样例
下面的例子中 T2 是 T1 的子树：

       1                3
      / \              /
T1 = 2   3      T2 =  4
        /
       4
下面的例子中 T2 不是 T1 的子树：

       1               3
      / \               \
T1 = 2   3       T2 =    4
        /
       4
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """

    def isSubtree(self, T1, T2):
        # write your code here
        if not T1 and not T2:
            return True
        if not T1:
            return False
        if not T2:
            return True
        if T1.val == T2.val:
            if self.check(T1, T2):
                return True
        if self.isSubtree(T1.left, T2):
            return True
        if self.isSubtree(T1.right, T2):
            return True
        return False

    def check(self, T1, T2):
        if not T1 and not T2:
            return True
        if not T1:
            return False
        if not T2:
            return False
        if T1 and T2 and T1.val == T2.val:
            return self.check(T1.left, T2.left) and self.check(T1.right, T2.right)
        return False
