class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []

    def push(self, val: int) -> None: #no return value so 
        self.stack.append(val)
         #checking if ministack is not empty
        if self.ministack == []:
            self.ministack.append(val)
        else:
            val = min(val, self.ministack[-1])
            self.ministack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.ministack.pop() #because the length of stack and ministack should be same. Else in second or more pop, the stack changes but min stack will remain same
        
    def top(self) -> int:
        value = self.stack[-1]
        return value
        
    def getMin(self) -> int:
        return self.ministack[-1]
        
        
