"""
key focus here was realizing that we could potentially pop the smallest element in the list as we traverse 
so we needed a way to remember the 2nd smallest element and we resolved this by creating a min stack which only gets appended whenever a new min element is encountered
whenever we popped the min element we would also pop from min_stack and have new min become min_stack[-1]
"""
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
