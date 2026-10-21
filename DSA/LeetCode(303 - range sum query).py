# Pattern : Here we add each and every element step by step and make a list. TO get answer of any queries, we just need one sabtraction.
class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix: list[int] = [0]
        for i in nums:
            self.prefix.append(self.prefix[-1]+i)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]