class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        unique = sorted(set(nums))
        current = 1
        largest = 0
        print(unique)
        prev = None

        for item in unique:
            if prev is not None and prev + 1 == item:
                current += 1
                print("increasing current to", current)
            else:
                largest = max(largest, current)
                current = 1
                print("updating largest to", largest)
            prev = item
        return max(largest, current)

