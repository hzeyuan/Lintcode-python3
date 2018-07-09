"""
380. 两个链表的交叉
请写一个程序，找到两个单链表最开始的交叉节点。

样例
下列两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
在节点 c1 开始交叉。

挑战
需满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    # 思路就是把两个链表对齐，然后找到他们相同的那个节点
    # time:1067ms
    def getIntersectionNode(self, headA, headB):
        # write your code here
        a = headA
        b = headB
        a1 = headA
        b1 = headB
        a_length = 0
        b_length = 0
        while a:
            a = a.next
            a_length += 1
        while b:
            b = b.next
            b_length += 1
        if a_length >= b_length:
            for _ in range(a_length-b_length):
                a1 = a1.next
        else:
            for _ in range(b_length - a_length):
                b1 = b1.next
        while a and b:
            if a.val == b.val:
                return ListNode(a.val)
        return
