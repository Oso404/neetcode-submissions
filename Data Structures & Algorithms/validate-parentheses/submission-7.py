class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        st = []
        for ch in s: 
            if ch not in dct:
               st.append(ch) 
            else:
                if not st:
                    return False
                cc = st.pop()
                if dct[ch] != cc:
                    return False
        return len(st) == 0