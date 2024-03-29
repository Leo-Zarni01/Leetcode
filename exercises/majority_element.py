import math
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maximum = math.floor(len(nums) / 2)
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        highest = 0
        for each in count.items(): ## each = (key, val)
            if each[1] > highest:
                highest = each[1]
                key = each[0]
        return key if highest > maximum else 0
    
    def majorityElementOther(self, nums: List[int]) -> int: ## this is boyer-moore majority vote algorithm
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != majority:
                count -= 1
            else:
                count += 1
        
            if count == 0:
                majority = nums[i]
                count = 1 ## reset
        return majority