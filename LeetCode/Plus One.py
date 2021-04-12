class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''
        s_list = []
        f_list = []
        z_list = []
        for i in digits:
        	i = str(i)
        	s_list.append(i)
        result = ''.join(s_list)
        result = int(result)
        result += 1
        result = str(result)
        for i in result:
        	f_list.append(i)
        for i in f_list:
        	i = int(i)
        	z_list.append(i)
        return z_list


obj = Solution()
print(obj.plusOne([1,2,3]))

