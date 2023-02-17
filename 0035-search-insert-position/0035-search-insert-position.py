class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        while(lo <= hi):
            mid = (hi + lo) // 2
            res = self.getDirection(nums, target, mid, lo, hi)
            if res == "found":
                return mid
            elif res == "left":
                hi = mid -1
            elif res == "right":
                lo = mid + 1
        return hi + 1 if target > lo else lo
    
    def getDirection(self, nums, target, mid, lo, hi):
        if nums[mid] == target:
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"