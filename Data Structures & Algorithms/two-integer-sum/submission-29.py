class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique = set(nums)

        for i, val in enumerate(nums):
            complement = target - val
            if complement in unique:
                print("current looking at i, val: ",i, val)
                print(f"complement of {complement} found in set")
                potentialDuplicate = val * 2 == target
                print(potentialDuplicate)
                for j in range(len(nums) - 1, i-1, -1):
                    if nums[j] == complement:
                        print("found", complement, "at index", j)
                        if potentialDuplicate and i == j: # 3+3 = 6 but so does 2+4. should continue
                            break
                        else:
                            return [i,j]
                    
        return []