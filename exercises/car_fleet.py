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
