"""
84. 落单的数 III
给出2*n + 2个的数字，除其中两个数字之外其他每个数字均出现两次，找到这两个数字。

样例
给出 [1,2,2,3,4,4,5,3]，返回 1和5

挑战
O(n)时间复杂度，O(1)的额外空间复杂度
"""


class Solution:
    """
    @param A : An integer array
    @return : Two integer
    """
    # 对于2n+1个数字用异或就行了，而在此题将所有数异或之后得到的是两个落单的数的异或结果，没办法将结果拆分成两个落单的数。
    # 但因为两个落单数不同，所以肯定存在某个位k，使得两落单数在第k位上一个为0另一个为1，怎么找到这个k?
    #  找异或结果中1出现的位置即可。只需找到最小的这个k，然后将在k位上为0的所有数做异或，其他的在k位为1的所有数也做另外的异或，
    # 这样最终可以得到两个落单的数。
    # time:1510ms
    def singleNumberIII(self, A):
        # write your code here
        s = 0
        for x in A:
            s ^= x
        # 找到那个存在的k位数字，使得两个数字在k位一个为0，另一个为1
        y = s & (-s)

        ans = [0, 0]
        # 将k位为0和1的数字分别异或，将结果存起来
        for x in A:
            if (x & y) != 0:
                ans[0] ^= x
            else:
                ans[1] ^= x
        return ans


s = Solution()
print(s.singleNumberIII([1, 2, 2, 3, 3, 5, 4, 4]))
