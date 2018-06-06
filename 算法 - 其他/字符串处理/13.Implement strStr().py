"""
13. Implement strStr()
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

样例
如果 source = "source" 和 target = "target"，返回 -1。

如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。

挑战
O(n2)的算法是可以接受的。如果你能用O(n)的算法做出来那更加好。（提示：KMP）
"""


class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    # time:1333ms
    """
    def strStr(self, source, target):
        if source is None:
            return -1
        elif target is "":
            return 0
        try:
            return source.index(target)
        except:
            return -1
    """

    """
    # 利用切片
    # time: 942ms
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:return -1
        if target is "" or target==source:return 0
        for i in range(len(source)-len(target)+1):
            if target == source[i:i+len(target)]:
                return i
        return -1        
    """
    # KMP,可以看看阮老师的博客
    # http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
    # time:1325 ms
    def strStr(self, source, target):
        if source is None or target is None: return -1
        if target is "" or target == source: return 0
        m = len(source)
        n = len(target)
        cur = 0  # 起始指针cur
        table = self.partial_table(target)
        while cur <= m - n:
            for i in range(n):
                if source[i + cur] != target[i]:
                    cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                    break
            else:
                return cur
        return -1

        # 部分匹配表

    def partial_table(self, p):
        prefix = set()
        postfix = set()
        table = [0]
        for i in range(1, len(p)):
            prefix.add(p[:i])
            postfix = {p[j:i + 1] for j in range(1, i + 1)}
            table.append(len((prefix & postfix or {''}).pop()))
        return table
