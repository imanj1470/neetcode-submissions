class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 1:
            mid = len(nums)// 2
            a = nums[:mid]
            b = nums[mid:]
            print(f"a: {a}, b: {b}")

            sA = a[0]
            eA = a[-1]
            sB = b[0]
            eB = b[-1]

            if sA > eA: #smallest lies within A
                nums = a
            elif sB > eB:
                nums = b
            else: #smallest lies on boundary, either sA OR sb
                return sA if sA < sB else sB
        return nums[0]
