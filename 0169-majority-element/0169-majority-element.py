class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        leng = len(nums)
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        inverse = [(value, key) for key, value in dictionary.items()]
        return max(inverse)[1]
        