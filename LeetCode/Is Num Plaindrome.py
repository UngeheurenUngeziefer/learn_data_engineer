class Solution(object):
    def isPalindrome(self, x):
        length = len(str(x))
        divider = int(length / 2)
        center_div = length // 2

        if len(str(x)) % 2 == 0:
            first_part = str(x)[0:divider]
            second_part = str(x)[divider::]
            if first_part == second_part[::-1]:
                return True
            else:
                return False
        elif len(str(x)) == 1:
            return True
        
        else:
            first_part = str(x)[0:center_div]
            second_part = str(x)[-center_div::]
            if first_part == second_part[::-1]:
                return True
            else:
                return False


