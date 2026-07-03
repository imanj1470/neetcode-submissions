class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        biggest = 0
        while i < j:
            amount = (j - i) * min(heights[i],heights[j])
            biggest = max(biggest, amount)
            print(f"i: {i} = {heights[i]}m,*  j: {j} = {heights[j]}m  === {amount}")

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return biggest