class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_s = min(strs)
        max_s = max(strs)
        if not min_s:
            return ""
        for i in range(len(min_s)):
            if max_s[i] != min_s[i]:
                return max_s[:i]
        return min_s[:]