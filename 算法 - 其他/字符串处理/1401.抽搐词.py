"""
1401. 抽搐词
我们正常的单词不会有连续两个以上相同的字母，如果出现连续三个或以上的字母，那么这是一个抽搐词。现在给一个单词，从左至右求出所有抽搐字母的起始点和结束点。

样例
给出 str = "whaaaaatttsup", 返回 [[2,6],[7,9]]。

解释：
"aaaa"和"ttt"是抽搐字母，输出他们的起始点和结束点。
给出 str = "whooooisssbesssst", 返回 [[2,5],[7,9],[12,15]]。
"""


class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """

    # time:1015ms
    def twitchWords(self, str):
        # Write your code here
        l = []
        i = 0
        while i < len(str) - 2:
            count = 1
            for j in range(i + 1, len(str)):
                if str[i] != str[j]:
                    break
                else:
                    count += 1
            if count >= 3:
                l.append([i, i + count - 1])
                i += count
            else:
                i += 1
        return l


s = Solution()
print(s.twitchWords("whaaaaatttsup"))
