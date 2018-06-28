"""
1292. Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

样例
Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: a singly linked list
    @return: Modified linked list
    """
    # time:984 ms
    def oddEvenList(self, head):
        # write your code here
        odd = ListNode(-1)
        odd_cur = odd
        even = ListNode(-1)
        even_cur = even
        count = 1
        while head:
            if count % 2 == 1:
                odd_cur.next = ListNode(head.val)
                odd_cur = odd_cur.next
            else:
                even_cur.next = ListNode(head.val)
                even_cur = even_cur.next
            count += 1
            head = head.next
        odd_cur.next = even_cur.next
        return odd.next


a5 = ListNode(5, )
a4 = ListNode(4, a5)
a3 = ListNode(3, a4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)
s =Solution()
print(s.oddEvenList(a1))