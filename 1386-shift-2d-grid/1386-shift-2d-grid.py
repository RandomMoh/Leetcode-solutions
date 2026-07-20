class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        
        if k == 0:
            return grid
            
        flat = [val for row in grid for val in row]
        flat = flat[-k:] + flat[:-k]
        
        return [flat[i * n : (i + 1) * n] for i in range(m)]