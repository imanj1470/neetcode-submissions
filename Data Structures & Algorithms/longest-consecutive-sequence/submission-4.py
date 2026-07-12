class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        unique = set(nums)
        print(unique)
        largest = 0
        for i in range(0, len(nums)):
            if nums[i] - 1 not in unique: #start of seq
                current = 1
                while nums[i] + current in unique:
                    current += 1
                largest = max(largest, current)

        return largest
