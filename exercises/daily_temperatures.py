from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [-1] * (len(temperatures))
        stack = []
        index = len(temperatures) - 1
        while index > -1:
            print("Current index: ", index)
            print("Results so far: ", results)
            print("Stack before update: ", stack)
            current = temperatures[index]
            print("Current temperature is: ", current)
            difference_index = None
            if len(stack) == 0:
                stack.append(index)
                print("Stack after update: ", stack)
                results[index] = 0
                print()
                index -= 1
                continue
            top = stack[-1]
            print("Top of stack index: ", top)
            temperature_from_top_stack = temperatures[top]
            print("From top stack, temperature is: ", temperature_from_top_stack)
            if temperature_from_top_stack > current:
                print("Top of stack is bigger")
                difference_index = top - index
                print("Difference is: ", difference_index)
                results[index] = difference_index
                stack.append(index)
            else:
                print("Top of stack is smaller")
                stack_index = len(stack) - 1
                stack_temperature_index = stack[stack_index]
                print(f"Is top of stack: {temperatures[stack_temperature_index]} smaller than current temperature: {current}? ", temperatures[stack_index] < current)
                while temperatures[stack_temperature_index] <= current:
                    print(f"{temperatures[stack_temperature_index]} vs {current}")
                    if len(stack) == 0:
                        results[index] = 0
                        break
                    else:
                        stack_index -= 1
                        stack_temperature_index = stack[stack_index]
                        stack.pop()
                    print("Stack after popping: ", stack)
                if len(stack) != 0:
                    top = stack[-1]
                    print("Top now is: ", top)
                    difference_index = top - index
                    print("Difference is: ", difference_index)
                    results[index] = difference_index
                stack.append(index)
            print("Stack at the end: ", stack)
            print()
            index -= 1
        print("Final results is: ", results)
        return results

## example_1 = Solution()
## temperatures = [30,38,30, 36, 35, 40, 28]
## results = example_1.dailyTemperatures(temperatures)

## example_1 = Solution()
## temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
## results = example_1.dailyTemperatures(temperatures)

## example_1 = Solution()
## temperatures = [33, 32, 31]
## results = example_1.dailyTemperatures(temperatures)

example_1 = Solution()
temperatures = [89,62,70,58,47,47,46,76,100,70]
results = example_1.dailyTemperatures(temperatures)
