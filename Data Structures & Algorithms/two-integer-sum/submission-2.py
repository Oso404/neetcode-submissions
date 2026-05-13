class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for index,num in enumerate(nums):
            if target - num not in store:
                store[num] = index
            else:
                return [store[target-num],index]
        