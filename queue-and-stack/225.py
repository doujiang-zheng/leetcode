from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        cnt = len(self.que)
        self.que.append(x)

        # move the last element to the first
        # push 4 into 3<---2<---1
        # 3<---2<---1<---4
        # 2<---1<---4<---3
        # 1<---4<---3<---2
        # 4<---3<---2<---1
        for _ in range(cnt):
            el = self.que.popleft()
            self.que.append(el)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.que[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.que) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()