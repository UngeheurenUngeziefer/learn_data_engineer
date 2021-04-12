class Solution(object):
    def runningSum(self, nums):
        new_list = []
        length = len(nums) + 1
        while len(new_list) != length:
        	for i in range(length):
        		new_list.append(sum(nums[0:i]))
        print(new_list[1::])

obj = Solution()
obj.runningSum([1,2,3,4])