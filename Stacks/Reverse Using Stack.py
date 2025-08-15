class Solution:
    def reverse(self, s: str) -> str:
        #code here 
        
        st = []
        
        for ch in s:
            st.append(ch)
            
        rev_str = ""
        
        while st:
            rev_str += st.pop()
            
        return rev_str
