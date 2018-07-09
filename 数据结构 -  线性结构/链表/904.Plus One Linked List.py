"""
904. Plus One Linked List
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

样例
Given head = 1 -> 2 -> 3 -> null, return 1 -> 2 -> 4 -> null
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    # 思路：翻转链表，然后加1,然后在翻转
    # 注意：999->1000,这种情况特殊
    # time:1616ms
    def plusOne(self, head):
        # Write your code here
        p = self.reverse(head)
        p1 = p
        while p1:
            if p1.val + 1 < 10:
                p1.val = p1.val + 1
                break
            else:
                p1.val = (p1.val + 1) % 10
                if not p1.next:
                    p1.next = ListNode(1)
                    break
                p1 = p1.next

        return self.reverse(p)

    def reverse(self, head):
        curt = None
        while head:
            # 下一个节点
            temp = head.next
            # 截出head的第一个结点指向curt
            head.next = curt
            curt = head
            # head长度减1，重复这个过程
            head = temp
        return curt


a3 = ListNode(9)
a2 = ListNode(9, a3)
a1 = ListNode(9, a2)
s = Solution()
print(s.plusOne(a1))
