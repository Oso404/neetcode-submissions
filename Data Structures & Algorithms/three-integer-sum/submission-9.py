"""
this is like 2 sum but with 2 pointers added
for each number we simply have 2 pointers (moving inward) after it and try to find the numbers that add up to required target
the hardest part was figuring out we had duplicates and we did this by incrementing/decrementing pointers if they encounter same number again 
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0-nums[i]
            lptr = i+1
            rptr = len(nums)-1
            while lptr < rptr:
                if nums[lptr] + nums[rptr] == target:
                    ret.append([nums[i], nums[lptr], nums[rptr]])
                    lptr+=1
                    rptr-=1
                    while lptr < rptr and nums[lptr] == nums[lptr - 1]:
                        lptr += 1

                    while lptr < rptr and nums[rptr] == nums[rptr + 1]:
                        rptr -= 1
                elif nums[lptr] + nums[rptr] < target:
                    lptr+=1
                else:
                    rptr-=1
        return ret