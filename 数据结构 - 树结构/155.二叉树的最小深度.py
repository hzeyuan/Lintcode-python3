"""
155. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

二叉树的最小深度为根节点到最近叶子节点的距离。
样例
给出一棵如下的二叉树:

        1

     /     \

   2       3

          /    \

        4      5

这个二叉树的最小深度为 2
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    # 递归
    # time:1691 ms
    def minDepth(self, root):
        # write your code here
        return self.find(root)

    def find(self, node):
        if node is None:
            return 0
        if node.left:
            left = self.find(node.left)
        else:
            return self.find(node.right) + 1

        if node.right:
            right = self.find(node.right)
        else:
            return left + 1

        return min(left, right) + 1


a3 = TreeNode(3)
a1 = TreeNode(2)
a1.left = a3

a = TreeNode(1)
a.left = a1
s = Solution()
print(s.minDepth(a))
