"""
175. 翻转二叉树
翻转一棵二叉树

样例
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4
挑战
递归固然可行，能否写个非递归的？
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    # time: 503 ms
    def invertBinaryTree(self, root):
        # write your code here
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
