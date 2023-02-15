import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            arr = [char for char in str(x)]
            if len(arr) == 1:
                return True
            for i in range(len(arr)):
                if arr[i] != arr[-i-1]:
                    return False
                if i+1 == math.ceil(len(arr) / 2):
                    return True
                    
    
        