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
        