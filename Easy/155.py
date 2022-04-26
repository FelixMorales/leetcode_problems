from collections import deque

class MinStack:

    def __init__(self):
        self.stack_i = -1
        self.min_stack_i = -1
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack_i +=1
        
        if self.min_stack_i < 0:
            self.min_stack.append(val)
            self.min_stack_i += 1
        else:
            if val <= self.min_stack[self.min_stack_i]:
                self.min_stack.append(val)
                self.min_stack_i += 1

    def pop(self) -> None:
        if self.stack[self.stack_i] == self.min_stack[self.min_stack_i]:
            self.min_stack.pop()
            self.min_stack_i -= 1

        self.stack.pop()
        self.stack_i -= 1



    def top(self) -> int:
        return self.stack[self.stack_i]
        

    def getMin(self) -> int:
        return self.min_stack[self.min_stack_i]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()