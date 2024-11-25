from typing import List
class Solution:
    def update(self, hash_key, hash_map, current_sequence):
        status = False
        print(f"hash_key: {hash_key} is in hash_map? {hash_key in hash_map}")
        if hash_key in hash_map and hash_map[hash_key] is False:
            hash_map[hash_key] = True
            current_sequence.append(hash_key)
            status = True
        return (hash_map, current_sequence, status)

    def longestConsecutive(self, nums: List[int]) -> int:
        visited = {}
        sequences = []
        for each_number in nums:
            visited[each_number] = False
        
        for index in range(len(nums)):
            current = nums[index]
            current_seq = [current]
            print("Current number is: ", current)

            next = current + 1
            print("Going forward...")
            for _ in range(index + 1, len(nums)):
                print("Current number to check is: ", next)
                updateRes = self.update(next, visited, current_seq)
                visited = updateRes[0] 
                current_seq = updateRes[1]
                status = updateRes[2]
                print("Status is: ", status)
                if status:
                    sequences.append(current_seq)
                else:
                    break
                next += 1

            prev = current - 1
            print("Going backward...")
            for _ in range(index + 1, len(nums)):
                print("Current number to check is: ", prev)
                updateRes = self.update(prev, visited, current_seq)
                visited = updateRes[0] 
                current_seq = updateRes[1]
                status = updateRes[2]
                print("Status is: ", status)
                if status:
                    sequences.append(current_seq)
                else:
                    break
                prev -= 1

            print("Sequence is: ", current_seq)
            sequences.append(current_seq)
            print()
        return max(map(len, sequences), default=0)

## demo_one = Solution()
## nums = [2,20,4,10,3,4,5]
## longest_csc_sq = demo_one.longestConsecutive(nums)
## print(longest_csc_sq)
## print("---------------")
## 
## demo_two = Solution()
## nums_two = [0,3,2,5,4,6,1,1]
## longest_csc_sq_two = demo_two.longestConsecutive(nums_two)
## print(longest_csc_sq_two)
## print("---------------")

demo_three = Solution()
nums_three = [9,1,4,7,3,-1,0,5,8,-1,6]
longest_csc_sq_three = demo_three.longestConsecutive(nums_three)
print(longest_csc_sq_three)
print("---------------")
