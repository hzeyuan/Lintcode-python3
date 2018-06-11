"""1270. Ransom Note Given an arbitrary ransom note string and another string containing letters from all the
magazines, write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
"""


class Solution:
    """
    @param ransomNote: a string
    @param magazine: a string
    @return: whether the ransom note can be constructed from the magazines
    """

    # time:2190 ms
    def canConstruct(self, ransomNote, magazine):
        # Write your code here
        letter = {chr(i): 0 for i in range(97, 123)}
        for i in ransomNote: letter[i] += 1
        for i in magazine: letter[i] -= 1
        for i in letter.values():
            if i > 0: return False
        return True
