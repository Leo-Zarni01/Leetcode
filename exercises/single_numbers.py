from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        counts = {}
        while i < len(nums):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1
            i += 1

        for key in counts.keys():
            if counts[key] == 1:
                return key
        return 1 
        
