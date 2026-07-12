class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        unique = set(nums)
        #print(unique)
        largest = 0
        for n in nums:
            if n - 1 not in unique: #start of seq
                current = 1
                while n + current in unique:
                    current += 1
                largest = max(largest, current)

        return largest
