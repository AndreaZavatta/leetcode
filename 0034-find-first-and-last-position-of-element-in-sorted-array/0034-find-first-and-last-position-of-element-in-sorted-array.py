class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findFirstOccurrence(nums, target), self.findLastOccurrence(nums, target)]
    
    def findFirstOccurrence(self, nums, target):
        lo = 0
        hi = len(nums)-1
        result = -1
        while(lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                result = mid
                hi = mid -1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid -1
        return result
    
    def findLastOccurrence(self, nums, target):
        lo = 0
        hi = len(nums)-1
        result = -1
        while(lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                result = mid
                lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid -1
        return result
    
  