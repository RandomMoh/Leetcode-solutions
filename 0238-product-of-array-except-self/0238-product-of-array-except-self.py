import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = np.array(nums, dtype=np.int64)
        prefix = np.concatenate(([1], np.cumprod(a[:-1])))
        suffix = np.concatenate((np.cumprod(a[::-1])[-2::-1], [1]))
        return (prefix * suffix).tolist()