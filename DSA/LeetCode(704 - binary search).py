# Pattern : Array is sorted. We take mid part and compare the value with target.so one comparison removes half of the range
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1
