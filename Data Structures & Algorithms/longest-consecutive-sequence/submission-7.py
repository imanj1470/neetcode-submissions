class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        unique = set(nums)
        largest = 0
        for n in unique:
            if n - 1 not in unique: #start of seq
                current = 0
                while n + current in unique:
                    current += 1
                largest = max(largest, current)

        return largest
