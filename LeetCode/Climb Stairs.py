class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        length_fib = n + 2
        fib_list = [0, 1]
        if n == 0:
        	return 0
        elif n == 1:
        	return 1
        else:
        	while len(fib_list) < length_fib:
        		sum_fin_nums = fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2]
        		fib_list.append(sum_fin_nums)
        	return fib_list[-1]


        	

obj = Solution()
print(obj.climbStairs(5))
