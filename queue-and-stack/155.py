class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) <= 0:
            self.stack.append((val, val))
        else:
            cur_min = min(val, self.stack[-1][1])
            self.stack.append((val, cur_min))
        

    def pop(self) -> None:
        el = self.stack.pop(-1)
        return el[0]
        

    def top(self) -> int:
        el = self.stack[-1]
        return el[0]

    def getMin(self) -> int:
        el = self.stack[-1]
        return el[1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()