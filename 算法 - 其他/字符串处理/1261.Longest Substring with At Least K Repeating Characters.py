"""  
1261. Longest Substring with At Least K Repeating Characters
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:

s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:

s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""


class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: return an integer
    """

    # 遍历整个数组，记录小于k次的的字母，把这些字母当成分割线来分割数组
    # 分割后的数组中的每一项都是竞争者，判断每一项中是否有出现小于k次的字母
    # ，有则继续以这个字母分割，然后把他们加入到竞争中，否的话，返回自己本身。
    # 最后返回长度最长的竞争者
    # time:1097ms
    def longestSubstring(self, s, k):
        # write your code here
        # 没有字符，k<0，跳出
        if not s or k < 0:
            return 0
        haxi = {}
        string = ''
       # 字符出现的次数
        for i in s:
            if i not in haxi:
                haxi[i] = 1
            else:
                haxi[i] += 1
        # 判断这个字符是否有小于k次的字符
        for i in haxi:
            if haxi[i] < k:
                string = i
        # 没有小于k次的字符，则返回本身
        if string == '':
            return len(s)
        else:
            # 有的话，以这个字符作为分割，遍历分割后产生的数组，作为竞争者加入
            maxlen = 0
            splits = s.split(string)
            for s in splits:
                maxlen = max(maxlen, self.longestSubstring(s, k))
        return maxlen


s = Solution()
print(s.longestSubstring("aaabbbacccbdc", 4))
