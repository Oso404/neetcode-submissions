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

