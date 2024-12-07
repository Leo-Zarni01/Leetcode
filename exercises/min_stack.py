from typing import List

class MinStack:

    def __init__(self):
        self.array = []

    def push(self, val: int) -> None:

    def pop(self) -> None:
        self.getArray().pop()

    def top(self) -> int:
        res = self.getArray()
        return res[0]

    def getMin(self) -> int:
        
    def getArray(self) -> List:
        return self.array
