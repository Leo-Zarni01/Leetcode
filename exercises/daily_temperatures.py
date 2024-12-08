import re
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        s1 = [temperatures[0]]
        results = []
        res = 0
        smaller_ctr = 0
        index = 1
        while len(results) != len(temperatures): 
            print("Results so far: ", results)
            current = temperatures[index]
            print(f"Current temperature is: {current}")
            top_s1 = s1[-1]
            print("s1 stack: ", s1)
            print("Top of s1 stack: ", top_s1)
            
            if index == len(temperatures) - 1:
                print("At the end of the road...")
                if current <= top_s1:
                    for _ in range(smaller_ctr):
                        results.append(0)
                else:
                    results.append(1)
                    results.append(0)
                break
            res += 1
            if current > top_s1:
                results.append(res)
                print(f"It is hot after {res} days")
                res = 0
                if len(s1) == 0:
                    s1.append(current)
                else:
                    index = len(s1)
                    print("Index is now at: ", index)
                    s1.append(temperatures[len(s1)])
                print("Updated stack, s1 is now: ", s1)
            else:
                smaller_ctr += 1
                print("Skip")
            print()
            index += 1
        print("Final results: ", results)
        return results

## example_1 = Solution()
## temperatures = [30,38,30, 36, 35, 40, 28]
## results = example_1.dailyTemperatures(temperatures)

example_1 = Solution()
temperatures = [33, 32, 31]
results = example_1.dailyTemperatures(temperatures)
