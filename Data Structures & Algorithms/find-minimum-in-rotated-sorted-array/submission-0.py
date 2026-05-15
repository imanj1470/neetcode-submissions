class Solution:
    def findMin(self, nums: List[int]) -> int:
        minx = nums[0]
        for num in nums:
            if num < minx:
                minx = num
        return minx
