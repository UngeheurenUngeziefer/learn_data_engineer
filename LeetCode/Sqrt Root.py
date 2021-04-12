import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x) // 1)

obj = Solution()
print(obj.mySqrt(8))
