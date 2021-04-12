class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs = reversed(s.strip())
        counter = 0
        for i in rs:
            if i != ' ':
                counter += 1
            elif s == ' ':
                return 0
            else:
                break
        return counter