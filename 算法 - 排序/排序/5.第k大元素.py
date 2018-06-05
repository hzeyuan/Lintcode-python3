"""
5. 第k大元素
在数组中找到第k大的元素

样例
给出数组 [9,3,2,4,8]，第三大的元素是 4

给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素是 4，第三大的元素是 3，以此类推

挑战
要求时间复杂度为O(n)，空间复杂度为O(1)
"""


class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    """
    # time:453ms
    def kthLargestElement(self, k, A):
        return sorted(A)[-k]
    """
    # 利用快排的思路,套模板了
    # time:325ms
    def kthLargestElement(self, k, A):
        return self.find_k(A, k, 0, len(A) - 1)

    def find_k(self, A, k, left, right):
        if left >= right:
            return A[k-1]
        low, high = left, right
        key = A[low]
        while left < right:
            while left < right and A[right] < key:
                right -= 1
            A[left] = A[right]
            while left < right and A[left] >= key:
                left += 1
            A[right] = A[left]
        A[right] = key
        if right == k-1:
            return A[k-1]
        elif right < k-1:
            return self.find_k(A, k, left + 1, high)
        elif right > k-1:
            return self.find_k(A, k, low, left - 1)


s = Solution()
print(s.kthLargestElement(3, [8, 3, 2, 4, 9]))
