class Solution(object):
	def removeDuplicates(self, nums):
		len_ = 1
		if len(nums) == 0:
			return 0
		for i in range(1, len(nums)):
			if nums[i] != nums[i-1]:
				nums[len_] = nums[i]
				len_ +=1
		return len_

obj = Solution()
print(obj.removeDuplicates([1, 1, 2]))