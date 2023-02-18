class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        HashNum = {}
        for num in nums:
            if num in HashNum:
                return True
            else:
                HashNum[num] = 1
        return False
        