"""
key here is that set lookup time is o(1)
we want to convert nums into set to make the above line possible
if (current_number-1) is not present ---> this means that this is the start of a sequence
----> if the if statement above is true we can have while look to look up (remember lookup here is o(1) for set) for num+1
----> update max accordinarly and return in the end
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        we need to identify the start of sequences.....
        list lookup time is o(n)
        set lookup time is o(1) *IMPORTANT*
        nums = [0,3,2,5,4,6,1,1]
        counter = 0

        0 
        is start? yes --> 0 : [0] counter++
        3
        is start? no --> 
        """
        if len(nums) == 0:
            return 0
        s = set(nums)
        oc = 1
        ic = 1
        for num in nums:
            if num-1 not in nums:
                start = num
                while start+1 in nums:
                   ic+=1
                   start+=1
                oc = max(oc,ic)
                ic = 1
            else:
                continue
        return oc

