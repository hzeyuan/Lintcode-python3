"""
167. 链表求和
你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。写出一个函数将两个整数相加，用链表形式返回和。

样例
给出两个链表 3->1->5->null 和 5->9->2->null，返回 8->0->8->null
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    # 思路：
    # 7 ----------------->1 ------------------>3 ---------------->5 ---------------------->null
    # 1 ----------------->2 ------------------>9 ---------------->7 ---------------------->8 ------ ---->6 --> null
    # 8 (7 + 1)--> 3(1 + 2)---> 2 进1(12)      --> 3进1(5 + 7 + 1 = 13)--> 9(8 + 1) --------> 6
    # time:764 ms
    def addLists(self, l1, l2):
        # write your code here
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
        return head
