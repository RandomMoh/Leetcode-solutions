class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix[0])
        l, r = 0, len(matrix) * n - 1
        
        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // n][mid % n]
            
            if val == target:
                return True
            if val < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False