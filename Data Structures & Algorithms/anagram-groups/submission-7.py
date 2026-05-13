class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = dict()
        grouped = [[]]
        #first solution i frequency counter...will do again 
        for word in strs:
            lst = [0] * 26
            for letter in word:
                ind = ord(letter.lower()) - ord('a')
                lst[ind] += 1
            tl = tuple(lst)
            if tl not in store:
                store[tl] = [word]
            else:
                store[tl].append(word)
        

        return list(store.values())