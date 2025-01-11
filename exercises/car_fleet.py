from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_data = {}
        for i in range(len(position)):
            car_data[position[i]] = speed[i]

        car_data = dict(sorted(car_data.items()))
        print(car_data)
        stack = []
        for car in reversed(car_data):
            print(f"Car position is: {car} and its speed is: {car_data[car]}")
            car_time = (target - car)/car_data[car]
            print("Time taken to reach target is: ", car_time)
            stack.append(car_time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            print()
        return len(stack)

## example_1 = Solution()
## position = [4,1,0,7]
## speeds = [2, 2, 1, 1]
## carFleet_1 = example_1.carFleet(10, position, speeds)

example_1 = Solution()
target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]
carFleet_1 = print(example_1.carFleet(target, position, speed))
