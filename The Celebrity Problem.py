class Solution:
    def celebrity(self, mat):
        # code here
        
        n = len(mat)
        
        a, b = 0,  n - 1
        
        while a < b:
            
            if mat[a][b] == 1:
                
                a += 1
                
            else:
                b -= 1
                
            
        cand = a
            
            
        for i in range(n):
            if i != cand:
                if mat[i][cand] == 0 or mat[cand][i] == 1:
                    return -1
                    
                    
        return cand
