class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        greatestNumber = len(nums)
        numsSum = greatestNumber * (greatestNumber+1) / 2
        tempSum = 0
        for n in nums:
            tempSum += n
        return numsSum - tempSum