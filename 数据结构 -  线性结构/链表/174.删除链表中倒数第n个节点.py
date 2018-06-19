"""
174. 删除链表中倒数第n个节点
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。



样例
给出链表1->2->3->4->5->null和 n = 2.

删除倒数第二个节点之后，这个链表将变成1->2->3->5->null.

挑战
O(n)时间复杂度
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    # time:1523ms
    def removeNthFromEnd(self, head, n):
        # write your code here
        if not head:
            return None
        ahead, btail = ListNode(-1), ListNode(-1)
        atail = ahead
        count = 1
        while head:
            atail.next = head
            atail = atail.next
            count += 1
            head = head.next
        btail = ahead.next
        if count-n ==1:
            return btail.next
        for i in range(1, count):
            if i == count - n:
                ahead.next = ahead.next.next
                break
            ahead = ahead.next
        return btail


a5 = ListNode(5)
a4 = ListNode(4, a5)
a3 = ListNode(3, a4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)
s = Solution()
print(s.removeNthFromEnd(a1, 5))
