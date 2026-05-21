class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        first number will always be the min of the stack
        [1] --> min=1 [1]
        [1,2] --> min=1 [1]
        [1,2,0] --> min=0 [1,0]
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    """
    what if what we popped is the min???
    -2 -2 -3 -3 
    """
    def pop(self) -> None:
        if not self.stack:
            return None
        sp = self.stack.pop()
        if sp == self.min_stack[-1]:
            self.min_stack.pop()
        
            

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
