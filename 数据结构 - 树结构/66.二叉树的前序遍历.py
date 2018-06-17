"""
66. 二叉树的前序遍历
给出一棵二叉树，返回其节点值的前序遍历。

样例
给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
 返回 [1,2,3].

挑战
你能使用非递归实现么？
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    # 前序遍历首先访问根结点然后遍历左子树，最后遍历右子树。在遍历左、右子树时，仍然先访问根结点，然后遍历左子树，最后遍历右子树。
    # time:569ms
    def preorderTraversal(self, root):
        # write your code here

        self.results = []
        self.traverse(root)
        return self.results

    def traverse(self, root):
        if root is None:
            return
        self.results.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


a3 = TreeNode(3)
a1 = TreeNode(2)
a1.left = a3
a = TreeNode(1)
a.right = a1
s = Solution()
print(s.preorderTraversal(a))
