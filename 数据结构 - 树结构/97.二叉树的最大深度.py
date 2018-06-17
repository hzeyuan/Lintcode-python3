"""
97. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的距离。

样例
给出一棵如下的二叉树:

  1
 / \
2   3
   / \
  4   5
这个二叉树的最大深度为3.
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
    # time:1305ms
    def maxDepth(self, root):
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

        return max(left, right) + 1

    """
    # 利用队列
    # time:1819 ms
    def maxDepth(self, root):
        # write your code here
        from collections import deque
        max_depth = 0
        if not root:
            return max_depth
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            max_depth += 1
        return max_depth
    """


a3 = TreeNode(3)
a1 = TreeNode(2)
a4 = TreeNode(4)
a1.left = a3
a1.right = a4
a = TreeNode(1)
a.right = a1
s = Solution()
print(s.maxDepth(a))
