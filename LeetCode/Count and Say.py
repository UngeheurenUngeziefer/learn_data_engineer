class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
		1.     1
		2.     11
		3.     21
		4.     1211
		5.     111221
        """

        def sequence(n):
            str_n = str(n)
            # '111221' -> 111 22 1
            counter = 0
            stack = []
            result = []
            for i in range(len(str_n)):
                if len(stack) == 0:
                    stack.append(str_n[i])
                elif str_n[i] in stack[len(stack) - 1]:
                    stack[len(stack) - 1] += str_n[i]
                elif str_n[i] not in stack[len(stack) - 1]:
                    stack.append(str_n[i])
            for i in stack:
                result.append(str(len(i)))
                result.append(i[0])
            res = ''.join(result)
            return res

        ress = 1
        sequence_stack = ['1']
        for i in range(30):
            ress = sequence(ress)
            sequence_stack.append(ress)

        return sequence_stack[n - 1]


obj = Solution()
print(obj.countAndSay(4))
