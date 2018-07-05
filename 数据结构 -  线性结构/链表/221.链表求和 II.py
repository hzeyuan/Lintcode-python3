"""
221. 链表求和 II
假定用一个链表表示两个数，其中每个节点仅包含一个数字。假设这两个数的数字顺序排列，请设计一种方法将两个数相加，并将其结果表现为链表的形式。

样例
给出 6->1->7 + 2->9->5。即，617 + 295。

返回 9->1->2。即，912 。
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """

    def reverse(self, linkedlist):
        curt = None
        while linkedlist:
            # 下一个节点
            temp = linkedlist.next
            # 截出head的第一个结点指向curt
            linkedlist.next = curt
            curt = linkedlist
            # head长度减1，重复这个过程
            linkedlist = temp
        return curt

    # 跟167题链表求和，唯一不同的地方是在于要翻转链表
    # time:1065ms
    def addLists2(self, l1, l2):
        # write your code here
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        n = 0
        head = ListNode(0)
        ptr = head
        while True:
            if l1:
                n += l1.val
                l1 = l1.next
            if l2:
                n += l2.val
                l2 = l2.next
            ptr.val = n % 10
            n //= 10
            if l1 or l2 or n != 0:
                ptr.next = ListNode(0)
                ptr = ptr.next
            # 退出的条件：没有l1,l2,同时n=0
            else:
                break
        return self.reverse(head)
