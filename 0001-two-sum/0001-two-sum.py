class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        myMap = {} #create hashmap
        res = [0, 0]
        
        for i, n in enumerate(nums):
            if n in myMap:
                res[0] = myMap[n]
                res[1] = i
            else:
                myMap[target-n] = i
        return res;