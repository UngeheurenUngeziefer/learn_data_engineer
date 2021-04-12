class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """      
        string = str(x)
            
        if string[0] == '-' and string[-1] != '0':
            string = string[1::]
            result = '-' + string[::-1]
            if int(result) < -2147483648:
                return 0
            else:
                return result
            

        elif string[0] == '-' and string[-1] == '0':
            string = string[1::]
            while string[-1] == '0':
                string = string[0:-1]
            result = '-' + string[::-1]
            if int(result) < -2147483648:
                return 0
            else:
                return result
            
        
        elif string[-1] == '0' and len(string) > 1:
            while string[-1] == '0':
                string = string[0:-1]
            result = string[::-1]
            if int(result) > 2147483648:
                return 0
            else:
                return result
        
        else:
            result = string[::-1]
            if int(result) > 2147483648:
                return 0
            else:
                return result
