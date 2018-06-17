"""
68. 二叉树的后序遍历
给出一棵二叉树，返回其节点值的后序遍历。

样例
给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
返回 [3,2,1]

挑战
你能使用非递归实现么？
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    # 后序遍历首先遍历左子树，然后遍历右子树，最后访问根结点，在遍历左、右子树时，仍然先遍历左子树，然后遍历右子树，最后遍历根结点。
    # time: 633ms
    def postorderTraversal(self, root):
        # write your code here
        self.results = []
        self.traverse(root)
        return self.results

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        self.results.append(root.val)
