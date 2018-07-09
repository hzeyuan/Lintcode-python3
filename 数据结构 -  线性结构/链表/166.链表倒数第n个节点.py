"""
166. 链表倒数第n个节点
找到单链表倒数第n个节点，保证链表中节点的最少数量为n。

样例
给出链表 3->2->1->5->null和n = 2，返回倒数第二个节点的值1.
"""


# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list.
    """
    # 返回的是节点，不是值
    # time: 1560ms
    def nthToLast(self, head, n):
        # write your code here
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        n = count - n
        for i in range(n):
            head = head.next
        return head.val


a1 = ListNode(1)
a2 = ListNode(2, a1)
a3 = ListNode(3, a2)
a4 = ListNode(4, a3)
s = Solution()
print(s.nthToLast(a4, 2))
