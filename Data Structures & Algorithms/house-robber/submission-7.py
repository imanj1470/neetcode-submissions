class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1] * len(nums)

        def checkRob(i):
            if i >= len(nums):
                return 0

            if mem[i] != -1:
                return mem[i]

            mem[i] = max(
                nums[i] + checkRob(i+2), 
                checkRob(i+1)
            )

            return mem[i]
        
        return checkRob(0)