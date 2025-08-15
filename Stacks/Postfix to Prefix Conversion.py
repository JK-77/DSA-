#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        
        stack = []
        
        for ch in post_exp:
            if ch.isalnum():
                stack.append(ch)
                
            else:
                
                op1 = stack.pop()
                op2 = stack.pop()
                
                new_exp = ch + op2 + op1
                stack.append(new_exp)
                
        return stack[-1]
