from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}
    for each_num in nums:
        if each_num not in counter:
            counter[each_num] = 1 # first appearance
        else:
            counter[each_num] += 1
    
    sorted_counter = sorted(counter.items(), key= lambda x:x[1], reverse=True)
    print(sorted_counter)

    res = []
    start = 0
    for each_key in sorted_counter:
        if start == k:
            break
        res.append(each_key[0])
        start += 1
    return res

nums = [1,2,2,3,3,3]
result = topKFrequent(nums, 2)
print(result)