class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        0 (48) --> 2 4 6
        1 (24) --> 1 4 6
        2 (12) --> 1 2 6
        3 (8) -->  1 2 4


        [1 | 2 4 6] [1 | 1 4 6] [1 | 1 2 6] [1 | 1 2 4]

        1 2 4 6 
        1 1 2 8 
        6 6 24 48

        48 24 12 

        6 4 2 1 
        6 6 24 48

        **prefix and suffix technique!!**
        **i have work on paper now easier to visualize**

        """
        pre = [1] * len(nums)
        post = [1] * len(nums)
        prods = [1] * len(nums)
        prod = 1
        #for prefix
        for index in range(1,len(nums)):
            prod*=nums[index-1]
            pre[index] = prod
        prod = 1
        for index in range(len(nums)-2,-1,-1):
            prod*=nums[index+1]
            post[index] = prod
        
        for i in range(len(pre)):
            prods[i] = pre[i] * post[i]

        return prods


            









