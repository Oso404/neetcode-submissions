# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ma = 0
#         """
#         *i see the words "maximum area" so that screams 2 pointer technique.
#         when can we trap water? min(blackbar1,blackbar2) > (everything in between)
#         1. have left ptr start at index 0 and traverse list until reach a black bar
#         2. have right ptr traverse starting from that index
#         --> while traversing must consider...
#         """
#         if not height:
#             return 0
        
#         return ma 
        
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res