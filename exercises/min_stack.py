class MinStack:
    def __init__(self):
        self.main_stack = []
        self.copy_stack = []

    def push(self, val: int) -> None:
        main_stack = self.get_main_stack()
        main_stack.append(val)

        copy_stack = self.get_copy_stack()
        if len(copy_stack) == 0:
            copy_stack.append(val)
            return

        top_copy_stack = self.copy_stack[-1]
        if val > top_copy_stack:
            copy_stack.append(top_copy_stack)
        else:
            copy_stack.append(val)
        return

    def pop(self) -> None:
        main_stack = self.get_main_stack()
        main_stack.pop()
        copy_stack = self.get_copy_stack()
        copy_stack.pop()

    def top(self) -> int:
        res = self.get_main_stack()
        return res[-1]

    def getMin(self) -> int:
        copy_stack = self.get_copy_stack()
        return copy_stack[-1]

    def get_main_stack(self):
        return self.main_stack

    def get_copy_stack(self):
        return self.copy_stack

example_1 = MinStack()
example_1.push(-2)
example_1.push(0)
example_1.push(-3)
min = example_1.getMin() ## -3
example_1.pop()
top_val = example_1.top()
