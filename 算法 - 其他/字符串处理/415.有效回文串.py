class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    # 类似的有491题
    # time:1256ms
    def isPalindrome(self, s):
        # write your code here
        left, right = 0, len(s.strip()) - 1
        s = s.lower()
        while left < right:
            while not s[left].isalpha() and not s[left].isdigit() and left < right:
                left += 1
            while not s[right].isalpha() and not s[right].isdigit() and left < right:
                right -= 1
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

