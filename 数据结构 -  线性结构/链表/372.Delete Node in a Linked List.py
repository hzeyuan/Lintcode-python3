"""
372. Delete Node in a Linked List
给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。

样例
Linked list is 1->2->3->4, and given node 3, delete the node in place 1->2->4
"""
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: the node in the list should be deletedt
    @return: nothing
    """
    # time:1009ms
    def deleteNode(self, node):
        # write your code here
        tmp = node.next
        node.val = tmp.val
        node.next = tmp.next
