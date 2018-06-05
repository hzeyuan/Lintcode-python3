"""
计算两个数组的交

样例
nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

挑战 What if the given array is already sorted? How would you optimize your algorithm? What if nums1's size is small
compared to num2's size? Which algorithm is better? What if elements of nums2 are stored on disk, and the memory is
limited such that you cannot load all elements into the memory at once? """


class Solution:
    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """
    #
    # time: 1836ms
    def intersection(self, nums1, nums2):
        # write your code here
        # 集合 + 基数排序
        # time:
        nums1_dict = {i: 0 for i in nums1}
        res = []
        for i in nums1:
            nums1_dict[i] += 1
        for j in nums2:
            try:
                if nums1_dict[j]:
                    res.append(j)
                    nums1_dict[j] -= 1
            except KeyError:
                continue
        return res

    # 排序 + 合并 ,跟两数组的交的方法三一样
    # time: 2323ms
    """
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        index1,index2 =0,0
        res = []
        while index1 <len(nums1) and index2 <len(nums2):
            if nums1[index1]<nums2[index2]:
                index1 +=1
            elif nums1[index1] >nums2[index2]:
                index2 +=1
            else:
                res.append(nums1[index1])
                index1 +=1
                index2 +=1
        return res
    """
