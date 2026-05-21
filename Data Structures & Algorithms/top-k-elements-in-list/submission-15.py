"""
we know that the most amount of times a number can appear is len(nums)
we could have double array[[]] with len(nums) number of inner arrays each to represent amount of times a number appears
we could have dict to keep track of number of number of times an element has appeared (orignally was thinking of sorting)
*dictionary* --> number:number_of_appearances
based on number of appearances will insert into ith inner array 
traverse backwards doubly array to get most frequent elements first (bucket sort technique where we have buckets)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lsts = [[] for _ in range(len(nums)+1)]
        d = dict() #key is number, value is count
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for num,count in d.items():
            lsts[count].append(num)
        res = []
        for i in range(len(lsts)-1,-1,-1):
            for x in lsts[i]:
                res.append(x)
                if len(res) == k:
                    return res
        