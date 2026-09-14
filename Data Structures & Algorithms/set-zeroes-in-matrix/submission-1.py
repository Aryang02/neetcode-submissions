class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            zero = False
            for j in range(n):
                if matrix[i][j] == 0:
                    zero = True
            
            for j in range(n):
                if zero and matrix[i][j] != 0:
                    matrix[i][j] = '#'
        
        for j in range(n):
            zero = False
            for i in range(m):
                if matrix[i][j] == 0:
                    zero = True
            
            for i in range(m):
                if zero and matrix[i][j] != 0:
                    matrix[i][j] = '#'
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0