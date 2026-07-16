class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for num in num_set:
            # Only start counting from the sequence's first element
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                best = max(best, length)

        return best