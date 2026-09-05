class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        localMin = 1
        localMax = 1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                localMin, localMax = 1,1#reset

            temp = localMax * nums[i]
            localMax = max(nums[i], localMax * nums[i], localMin * nums[i])
            localMin = min(nums[i], localMin * nums[i], temp)

            maxProd = max(maxProd, localMax)
        return maxProd







                
