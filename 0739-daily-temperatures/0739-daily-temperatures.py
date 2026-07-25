class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev_i = stack.pop()
                ans[prev_i] = i - prev_i
            stack.append(i)
            
        return ans