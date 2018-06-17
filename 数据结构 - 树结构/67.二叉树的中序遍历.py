"""
67. 二叉树的中序遍历
给出一棵二叉树,返回其中序遍历

样例
给出二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
返回 [1,3,2].

挑战
你能使用非递归算法来实现么?
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    # 中序遍历首先遍历左子树，然后访问根结点，最后遍历右子树
    # time:573ms
    def inorderTraversal(self, root):
        # write your code here
        self.results = []
        self.traverse(root)
        return self.results

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.results.append(root.val)
        self.traverse(root.right)


a3 = TreeNode(3)
a1 = TreeNode(2)
a1.left = a3
a = TreeNode(1)
a.right = a1
s = Solution()
print(s.inorderTraversal(a))