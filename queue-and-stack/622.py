class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.start = 0
        self.end = 0
        self.cnt = 0
        self.que = [0 for _ in range(k)]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.que[self.end] = value
        self.end = (self.end + 1) % self.size
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False        
        self.start = (self.start + 1) % self.size
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        idx = (self.end - 1 + self.size) % self.size
        return self.que[idx]

    def isEmpty(self) -> bool:
        return self.cnt == 0  

    def isFull(self) -> bool:
        return self.cnt == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()