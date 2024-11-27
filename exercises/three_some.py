from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sols = []
        for _ in range(len(numbers)):
            left_num = numbers[left]
            right_num = numbers[right]
            print("Left num is: ", left_num)
            print("Right num is: ", right_num)
            if left > right:
                break
            else:
                if left_num + right_num > target:
                    right -= 1
                elif left_num + right_num < target:
                    left += 1
                elif left_num + right_num == target:
                    print("VALID PAIR!!")
                    sols.append([left, right]) ## indices
                    left += 1
                    right -= 1
        return sols

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()

        for index in range(len(nums)):
            curr = nums[index]
            print("Current number is: ", curr)
            sol = [curr]
            target = 0 - curr
            print("Target is: ", target)
            look_up_arr = nums[index + 1:]
            print("look_up_arr is: ", look_up_arr)
            valid_pairs = self.twoSum(look_up_arr, target)
            print(valid_pairs)
            if len(valid_pairs) > 0:
                for each_pair in valid_pairs:
                    print(each_pair)
                    ## first_number = each_pair[0] + 1
                    ## second_number = each_pair[1] + 1
                    ## sol.append(first_number)
                    ## sol.append(second_number)
                    ## if sol not in solutions:
                    ##     solutions.append(sol)
            print()
        return solutions

## demo_one = Solution()
## nums=[-1,0,1,2,-1,-4]
## test_one = demo_one.threeSum(nums)
## print(test_one)
## print()
## 
## print("BREAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK")
## print()
## 
## demo_two = Solution()
## nums_two=[0, 0, 0]
## test_two = demo_two.threeSum(nums_two)
## print(test_two)
## 
## print("BREAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK")
## print()

## demo_three = Solution()
## nums_three=[0, 0, 0, 0]
## test_three = demo_three.threeSum(nums_three)
## print(test_three)

demo_four = Solution()
nums_four = [-2,0,1,1,2]
test_four = demo_four.threeSum(nums_four)
print(test_four)
