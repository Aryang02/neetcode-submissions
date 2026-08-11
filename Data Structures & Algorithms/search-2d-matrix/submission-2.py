class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        for i in range(len(matrix)):
            j, k = 0, len(matrix[i])-1
            if matrix[i][j] == target or matrix[i][k] ==target:
                return True
            if matrix[i][k] < target:
                continue
            while j < k:
                mid = (j+k)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    j = mid+1
                else:
                    k = mid-1
        return res