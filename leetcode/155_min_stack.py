class MinStack:

    stack = []
    currentMin = 0

    def __init__(self):
        self.stack = []
        self.currentMin = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.setCurrentMin()

    def pop(self) -> None:
        self.stack.pop()
        self.setCurrentMin()

    def top(self) -> int:
        vall = self.stack.pop()
        self.stack.append(vall)
        return vall

    def getMin(self) -> int:
        return self.currentMin
    
    def setCurrentMin(self):
        self.currentMin = None
        for vall in self.stack:
            if self.currentMin is None or vall <= self.currentMin:
                self.currentMin = vall
                


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print("MIN1: ", obj.getMin())
    obj.pop()
    print("TOP:", obj.top())
    print("MIN2: ", obj.getMin())
    
    
    obj2 = MinStack()
    obj2.push(-1)
    obj2.top()
    print(obj2.getMin())
