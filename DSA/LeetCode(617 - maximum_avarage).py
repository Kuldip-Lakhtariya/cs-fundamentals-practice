# Pattern : Here for window size k instead of doing sum every time, we just take that sum and subtract the former elemt and add new element.
class Solution:
    def findMaxAverage(self, nums: list[int],k : int) -> float:
        window_sum = sum(nums[:k])
        best = window_sum
        for i in range (k,len(nums)):
            window_sum += nums[i] - nums[i-k]
            best = max(best,window_sum)
        return best/k

