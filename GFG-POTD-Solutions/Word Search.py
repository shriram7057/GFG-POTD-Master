class Solution:
	def isWordExist(self, mat, word):
		# Code here
		n = len(mat)
		m = len(mat[0])
		
		def dfs(i,j,idx):
		    if idx == len(word):
		        return True
		    if i < 0 or i >= n or j < 0 or j>= m or mat[i][j] != word[idx]:
		        return False
		    temp = mat[i][j]
		    mat[i][j] = '#'
		    
		    found = (dfs(i+1,j,idx+1) or 
		            dfs(i - 1,j,idx + 1) or 
		            dfs(i,j + 1,idx + 1) or 
		            dfs(i,j - 1,idx + 1))
		    mat[i][j] = temp
		    return found
		for i in range(n):
		    for j in range(m):
		        if mat[i][j] == word[0]:
		            if dfs(i,j,0):
		                return True
		return False