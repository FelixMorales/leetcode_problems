from collections import deque

class Node:
    def __init__(self):
        self.minUntilMe = None
        self.val = None
        
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.length = 0
        

    def push(self, val: int) -> None:
        newNode = Node()
        if self.length:
            if(self.stack[self.length - 1].minUntilMe > val):
                newNode.minUntilMe = val
            else:
                newNode.minUntilMe = self.stack[-1].minUntilMe
        else:
            newNode.minUntilMe = val
        newNode.val = val
        self.length += 1
        self.stack.append(newNode)
        

    def pop(self) -> None:
        self.length -= 1
        to_return = self.stack.pop()
            
        return to_return.val
        

    def top(self) -> int:
        return self.stack[self.length-1].val
        

    def getMin(self) -> int:
        return self.stack[self.length-1].minUntilMe