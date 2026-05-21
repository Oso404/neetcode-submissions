
"""
main thing here is that a set removes duplicates; l8er on we see that it also have o(1) lookup time
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       return len(nums) != len(set(nums))
