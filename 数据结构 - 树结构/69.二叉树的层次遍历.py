"""
69. 二叉树的层次遍历
给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）

样例
给一棵二叉树 {3,9,20,#,#,15,7} ：

  3
 / \
9  20
  /  \
 15   7
返回他的分层遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
挑战
挑战1：只使用一个队列去实现它

挑战2：用DFS算法来做
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    """
        # 方式1：
        def levelOrder(self, root):
        # write your code here
        results = []
        if not root:
            return results
        res = [root]
        while res:
            new_list = []
            results.append([n.val for n in res])
            for node in res:
                if node.left:
                    new_list.append(node.left)
                if node.right:
                    new_list.append(node.right)
            res = new_list
        return results
    """
    # 利用队列
    # 先将二叉树添加进队列，然后通过不断popleft树的当前跟结点，同时添加当前树的左子树和右子树进队列，重复这个过程，直到队列中没有元素。
    # time:884 ms
    def levelOrder(self, root):
        # write your code here
        from collections import deque
        result = []
        if root is None:
            return result
        q = deque([root])
        while q:
            result.append([item.val for item in q])
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result


a3 = TreeNode(3)
a1 = TreeNode(2)
a4 = TreeNode(4)
a1.left = a3
a1.right = a4
a = TreeNode(1)
a.right = a1
s = Solution()
print(s.levelOrder(a))
