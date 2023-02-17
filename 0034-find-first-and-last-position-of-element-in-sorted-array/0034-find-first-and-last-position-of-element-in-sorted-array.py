class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findFirstOccurrence(nums, target), self.findLastOccurrence(nums, target)]
        
    def findFirstOccurrence(self, nums, target):
        hi = len(nums) - 1
        lo = 0
        result = -1
        while(lo <= hi):
            
            mid = (hi + lo) // 2
            if nums[mid] == target:
                result = mid
                hi = mid -1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return result
    
    def findLastOccurrence(self, nums, target):
        hi = len(nums) - 1
        lo = 0
        result = -1
        while(lo <= hi):
            mid = (hi + lo) // 2
            if nums[mid] == target:
                result = mid
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return result  
