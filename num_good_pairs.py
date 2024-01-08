from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ## cannot sort it as that would mess up the ordering of the array
        counts = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr not in counts:
                counts[curr] = 1
            else:
                counts[curr] += 1

        res = 0
        for j in counts.keys():
            # print(f"{j}: {counts[j]}")
            if counts[j] > 1:
                for k in range(counts[j] - 1, 0, -1):
                    # print("k: ", k)
                    res += k
        return res