"""
1005. Largest Triangle Area
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:

Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


样例
3 <= points.length <= 50.
No points will be duplicated.
-50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
"""


class Solution:
    """
    @param points: List[List[int]]
    @return: return a double
    """
    # 三角形面积公式：S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
    # time: 1266 ms
    def largestTriangleArea(self, points):
        # write your code here
        max_area = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    area = 0.5 * abs((
                                points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][1]
                                - points[i][0] * points[k][1] - points[j][0] * points[i][1] - points[k][0] * points[j][
                                    1]))
                    if area > max_area:
                        max_area = area
        return max_area

s = Solution()
print(s.largestTriangleArea([[6,3],[5,2],[5,8],[0,6]]))
