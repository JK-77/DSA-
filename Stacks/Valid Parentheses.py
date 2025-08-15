class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []
        match = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in "({[":
                st.append(ch)
            else:
                if not st or st[-1] != match[ch]:
                    return False

                st.pop()

        return not st
