"""
547. 两数组的交
返回两个数组的交

样例
nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].

挑战
可以用三种不同的方法实现吗？
"""


class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    # 方法一
    # time: 1625ms
    def intersection(self, nums1, nums2):
        nums1, nums2 = set(nums1), set(nums2)
        return list(nums1 & nums2)

    # 方法二
    # 排序加 + 二分查找
    # time: 3204ms
    """
    def intersection(self, nums1, nums2):
        if not nums1:
            return nums1
        elif not nums2:
            return nums2
        else:
            nums1.sort()
        res = set()
        for i in nums2:
            if not nums1:
                return nums2
            left, right = 0, len(nums1)-1
            while left <= right:
                mid = (left + right) // 2
                if i > nums1[mid]:
                    left = mid + 1
                elif i < nums1[mid]:
                    right = mid - 1
                else:
                    res.add(i)
                    break
        return list(res)
    """

    # 方法三
    # 排序 + 合并
    # time: 2230ms
    """
    def intersection(self, nums1, nums2):
        if nums1 and nums2:
            nums1.sort()
            nums2.sort()
            res = set()
            n1, n2 = 0, 0
            while n1 < len(nums1) and n2 < len(nums2):
                if nums1[n1] > nums2[n2]:
                    n2 += 1
                elif nums1[n1] == nums2[n2]:
                    res.add(nums1[n1])
                    n1 += 1
                    n2 += 1
                elif nums1[n1] < nums2[n2]:
                    n1 += 1
        elif not nums1:
            return nums1
        elif not nums2:
            return nums2
        return list(res)
    """


    # 参考
    # 暴力
    # time: 超时了
    """
        def intersection(self, nums1, nums2):
            res = set()
            for i in nums2:
                if i in nums1:
                    res.add(i)
            return list(res)
    """


s = Solution()
print(s.intersection([21, 3, 4], [1]))
x =0
nums1_dict = {i: i for i in [1,2,3,1]}
print(dict(nums1_dict))