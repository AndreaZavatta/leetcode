import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        negative = False;
        if(x < 0):
            negative = True
            x *= -1
        arr = [char for char in str(x)]
        print(arr)
        for i in range(len(arr)-1, -1,-1):
            res += int(arr[i]) * math.pow(10,i)
            if(res <= math.pow(-2, 31) or res >= math.pow(2, 31)-1):
                return 0
            print(res)
        return  int(res) if not negative else int(res) * -1