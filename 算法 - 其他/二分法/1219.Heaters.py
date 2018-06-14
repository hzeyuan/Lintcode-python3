"""
1219. Heaters
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum
radius standard of heaters.

样例
Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""


class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """

    def findRadius(self, houses, heaters):
        # Write your code here
        pass
        max_radius = max(heaters[0] - houses[0], houses[-1] - heaters[-1])
        if len(heaters) == 1:
            return max_radius
        for i in range(1, len(heaters)):
            if (heaters[i] - heaters[i - 1] - 1) // 2 > max_radius:
                max_radius = (heaters[i] - heaters[i - 1] - 1) // 2
        return max_radius


s = Solution()
print(s.findRadius([1, 2, 3,4], [1,4]))
