"""1038. Jewels and Stones You're given strings J representing the types of stones that are jewels,
and S representing the stones you have. Each character in S is a type of stone you have. You want to know how many of
the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".

样例
Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
"""


class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    # time:851ms
    def numJewelsInStones(self, J, S):
        # Write your code here
        set = {i for i in J}
        count = 0
        for i in S:
            if i in set:
                count += 1

        return count


s = Solution()
print(s.numJewelsInStones("aA","aAAbbbb"))
